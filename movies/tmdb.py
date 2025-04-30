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

import os


API_KEY = os.getenv("TMDB_API_KEY")
BASE    = "https://api.themoviedb.org/3"
IMG_CDN = "https://image.tmdb.org/t/p/w185"

def _fetch(endpoint, query):
    params = {"api_key": API_KEY, "query": query, "include_adult": False}
    data = requests.get(f"{BASE}{endpoint}", params=params, timeout=7).json()
    return data.get("results") or []


def search_tmdb_multi(query: str, limit: int = 6):
    """
    Return a merged list of movie + tv hits:
      [{title, year, poster, media_type}, …]
    """
    movies = _fetch("/search/movie", query)
    shows  = _fetch("/search/tv",    query)

    def remap(item, media):
        title = item["title"] if media == "movie" else item["name"]
        year  = (item.get("release_date") or item.get("first_air_date") or "")[:4]
        poster = item["poster_path"]
        poster_url = f"{IMG_CDN}{poster}" if poster else None
        return {
            "title": title,
            "year":  year,
            "poster": poster_url,
            "media_type": media,   # movie | tv
        }

    merged = [*map(lambda x: remap(x, "movie"), movies[:limit//2]),
              *map(lambda x: remap(x, "tv"),    shows[:limit//2])]

    # sort by TMDB popularity desc
    merged.sort(key=lambda d: d["title"])
    return merged[:limit]


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