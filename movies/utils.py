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

import requests

from django.conf import settings

# Custom model to store movies
from .models import Movie

# Created a reusable script that can pull data from the TMDB API
def fetch_and_save_movie(title):

    url = f"https://api.themoviedb.org/3/search/movie?api_key={settings.TMDB_API_KEY}&query={title}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        results = data.get("results")

        if results:
            movie_data = results[0] # Gets the first matching result
            tmdb_id = movie_data["id"]

            # Creates and saves the movie in the local database
            movie = Movie.objects.create(

                title=movie_data["title"],
                tmdb_id=tmdb_id,
                poster_url=f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}" if movie_data.get("poster_path") else "",
                description=movie_data.get("overview", ""),
                release_date=movie_data.get("release_date", None)

            )

            return movie

    return None # Returns nothing if movie was not found
