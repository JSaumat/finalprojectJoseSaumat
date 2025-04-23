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

from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

# This allows for the reference to the URLS below
app_name = 'movies'

# Adds url for each page on the site
urlpatterns = [

    # The Home page
    path('', views.index, name='index'),

    # Movie import for voting page (admin only)
    path('search/', views.search_movie, name='search_movie'),

    # Voting for a specific movie page
    path('vote/<int:movie_id>/', views.vote_movie, name='vote_movie'),

    # User registration page
    path('register/', views.register_user, name='register'),

    # Login page
    path('login/', views.login_user, name='login'),

    # Logout page
    path("logout/", views.logout_view, name="logout"),

    # Logout confirmation page
    path("logged_out/", views.logged_out_view, name="logged_out"),

    # About the site page
    path("about/", views.about_page, name="about"),

    # Quick search bar in the navigation bar to search the TMDB database
    path("quick-lookup/", views.quick_lookup, name="quick_lookup"),

    # Test to check if API key was working during development
    #path('test-api/', views.test_api_key, name='test_api'),

    # Test to check if TMDB API integration was working during development
    #path('import/', views.import_movie),

]