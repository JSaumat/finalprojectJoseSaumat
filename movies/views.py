'''

INF601 - Programming in Python

Assignment #3:  Mini Project 4

I,     Jose Saumat   , affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism,
or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have
accurately cited all sources in adherence to academic standards. I understand that failing to comply with this
integrity statement may result in consequences, including disciplinary actions as determined by my course instructor
and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles
of academic integrity.

'''

from django.conf import settings
from .tmdb_client import get_movie, search_id


# Django imports for handling HTTP requests and handling templates

from django.shortcuts import render

from django.shortcuts import get_object_or_404, redirect

from django.db.models import F

from django.shortcuts import redirect

from django.http import HttpResponse

# Imports custom forms or models

from .forms import MovieSearchForm

from .forms import RegisterForm, LoginForm

from .models import Movie

from .utils import fetch_and_save_movie

# Authentication and Permissions

from django.contrib.auth import login, authenticate, logout

from django.contrib import messages

from django.contrib.auth.decorators import user_passes_test

from django.core.exceptions import PermissionDenied

from django.conf import settings

# Disables CSRF protection for quick API lookups in development
from django.views.decorators.csrf import csrf_exempt

# Imports the TMDB search utility
from .tmdb import search_tmdb

# Imports the Movie and MovieVote classes
from .models import Movie, MovieVote

from django.contrib.auth.decorators import login_required

from django.views.decorators.http import require_POST

from django.db.models import Count, Q

from .tmdb_client import get_movie



# Used to test TMDB API integration earlier in development
# from .utils import fetch_and_save_movie

# Test to see if API key was working
# def test_api_key(request):
#     return HttpResponse(f"API Key: {settings.TMDB_API_KEY}")

# Used to test TMDB API integration
# def import_movie(request):
#     movie = fetch_and_save_movie("The Matrix")
#     if movie:
#         return HttpResponse(f"Imported movie: {movie.title}")
#     return HttpResponse("Movie not found.")

# Create your views here.
def index(request):

    return render(request, 'movies/movie_voting.html')

# Checks to make sure user is authorized to access page if not throws 403 error
def only_admin(user):

    if not user.is_authenticated or not (user.is_superuser or user.is_staff):

        raise PermissionDenied

    return True

# Creates the view to search for movies that only superusers or admins can access
@user_passes_test(only_admin)
def search_movie(request):

    form = MovieSearchForm()

    message = ""

    if request.method == "POST":

        # Handles submission from either the MovieSearchForm or the navbar input
        title = request.POST.get("title")

        if title:
            movie = fetch_and_save_movie(title)

            if movie:
                message = f"Movie '{movie.title}' imported successfully!"

            else:
                message = "Movie not found or could not be imported."

        else:
            message = "Please enter a movie title."

    return render(request, "movies/search.html", {"form": form, "message": message})

# Adds the movie view in index
def index(request):
    # 1️⃣  fetch all movies
    movies = Movie.objects.all().order_by('-release_date')

    # 2️⃣  NEW — store the current user’s vote on each movie instance
    for m in movies:
        m.my_vote = m.user_vote(request.user)

    voted_movie     = request.session.pop('voted', None)
    login_required  = request.session.pop('login_required', False)

    return render(request, 'movies/movie_voting.html', {
        'movies': movies,
        'voted_movie': voted_movie,
        'login_required': login_required,
    })


# Adds the voting view
@login_required
@require_POST
def movie_vote(request, movie_id):
    action = request.POST.get("action")          # "like" | "dislike"
    movie  = get_object_or_404(Movie, id=movie_id)
    value  = MovieVote.LIKE if action == "like" else MovieVote.DISLIKE

    obj, created = MovieVote.objects.update_or_create(
        user=request.user, movie=movie,
        defaults={"value": value},
    )

    # Toggle OFF if the user clicked the same filled button again
    if not created and obj.value == value and request.POST.get("toggle") == "1":
        obj.delete()

    return redirect("movies:index")              # back to movie-voting page

# Adds the user registration view
def register_user(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            # Prevents from writing to DB
            user = form.save(commit=False)

            # Hashes the users password
            user.set_password(form.cleaned_data['password'])

            form.save()

            # Set flag for modal if registration successful
            request.session['registered'] = True
            return redirect('movies:login')

    else:

        form = RegisterForm()

    return render(request, 'movies/register.html', {'form': form})

# Adds the user login view
def login_user(request):

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            user = authenticate(

                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:

                login(request, user)

                return redirect('movies:home')

        # Set flag for modal display if login fails
        request.session['login_failed'] = True
        return redirect('movies:login')

    else:

        form = LoginForm()

    # Clear the session flag after displaying modal
    login_failed = request.session.pop('login_failed', None)
    registered = request.session.pop('registered', None)

    return render(request, 'movies/login.html', {

        'form': form,
        'login_failed': login_failed,  # <-- send to template context
        'registered': registered

    })

# Adds the log-out user view
def logout_view(request):

    logout(request)

    return redirect("movies:logged_out")

# Adds logged out page confirmation view
def logged_out_view(request):

    return render(request, "movies/logged_out.html")

#Adds about page view
def about_page(request):

    return render(request, "movies/about.html")

# Adds a lookup to search TMDB without adding to the index voting page
@csrf_exempt
def quick_lookup(request):

    results = []
    query = ""

    if request.method == "POST":

        query = request.POST.get("title")

        if query:

            results = search_tmdb(query)

    return render(request, "movies/quick_lookup_results.html", {

        "results": results,
        "query": query

    })

#Original test homepage before implementing the API powered version below
# def home(request):
#     movies = [
#         # title, trailer URL, poster URL  (replace with your data)
#         ("The Dark Knight", "https://youtu.be/EXeTwQWrcwY",
#          "https://image.tmdb.org/t/p/w342/qJ2tW6WMUDux911r6m7haRef0WH.jpg"),
#         ("Inception", "https://youtu.be/YoHD9XEInc0",
#          "https://image.tmdb.org/t/p/w342/edv5CZvWj09upOsy2Y6IwDhK8bt.jpg"),
#         # …add 8 more …
#     ]
#     return render(request, "movies/index.html", {"movies": movies})

# New Home Page view
def home(request):
    movies = []
    for title, year in settings.FAVORITE_MOVIES:
        mid = search_id(title, year)
        if mid:
            movies.append(get_movie(mid))
        else:
            movies.append({
                "title": f"{title} ({year or '?'})",
                "poster": None,
                "trailer": "#",
            })
    return render(request, "movies/index.html", {"movies": movies})


# Leaderboard for community votes
def leaderboard(request):
    movies = (
        Movie.objects
        .annotate(like_count=Count("votes", filter=Q(votes__value=MovieVote.LIKE)))
        .filter(like_count__gt=0)
        .order_by("-like_count", "title")[:10]
    )

    # NEW: fetch trailer URLs via TMDB helper (cached)
    for m in movies:
        details = get_movie(m.tmdb_id)
        m.trailer = details["trailer"]

    return render(request, "movies/leaderboard.html", {"movies": movies})
