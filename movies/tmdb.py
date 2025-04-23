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

# Used to make requests from the TMDB API
import requests

# Used to access TMDB API key from settings.py
from django.conf import settings

# Search TMDB for a movie by title in the navigation bar (quick lookup version)
def search_tmdb(query):

    url = f"https://api.themoviedb.org/3/search/movie"

    params = {

        "api_key": settings.TMDB_API_KEY,
        "query": query

    }

    response = requests.get(url, params=params)

    if response.status_code == 200:

        #Parses JSON response and display top 12 results
        data = response.json()

        return data.get("results", [])[:12]  # Return top 12 results

    return [] # If the API call fails