'''

INF601 - Programming in Python

Assignment:  Final Project

I,     Jose Saumat   , affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism,
or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have
accurately cited all sources in adherence to academic standards. I understand that failing to comply with this
integrity statement may result in consequences, including disciplinary actions as determined by my course instructor
and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles
of academic integrity.

'''

#These classes are used to generate forms and handle user input

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm

from django import forms

from .models import Movie

# Original Movie search form for movies only
class MovieSearchForm(forms.Form):

    """
    Single text input for searching TMDB movies; used by /search/ page.
    """

    title = forms.CharField(

        max_length=100,

        label="Movie Title",

        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

# Revised Movie and TV Show search form
class MediaSearchForm(forms.Form):

    """
    Title + media type selector (Movie | TV Show). Used on Add Movie / TV page.
    """

    title = forms.CharField(max_length=200, label="Title")

    # Reuse of model constants to keep form in sync
    MEDIA_CHOICES = (

        (Movie.MOVIE, "Movie"),
        (Movie.TV,    "TV Show"),

    )
    media_type = forms.ChoiceField(

        choices=MEDIA_CHOICES,
        initial=Movie.MOVIE,
        label="Media type",

    )


# Registration form for user sign-up
class RegisterForm(forms.ModelForm):

    """
    Wraps the built‑in User model to collect username / email / password.
    """

    username = forms.CharField(

        max_length=150,

        widget=forms.TextInput(attrs={'class': 'form-control'})

    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # User class which takes username, email, and password
    class Meta:

        model = User

        fields = ['username', 'email', 'password']

# Log-in form that swaps BootStrap styled widgets
class LoginForm(AuthenticationForm):

    username = forms.CharField(

        widget=forms.TextInput(attrs={'class': 'form-control'}),

        label="Username"

    )
    password = forms.CharField(

        widget=forms.PasswordInput(attrs={'class': 'form-control'}),

        label="Password"

    )