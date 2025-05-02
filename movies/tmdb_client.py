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

# movies/tmdb_client.py
import os, requests, functools

# Module level constants
API_KEY = os.getenv("TMDB_API_KEY")            # already loaded from .env
BASE    = "https://api.themoviedb.org/3"
IMG_CDN = "https://image.tmdb.org/t/p/w342"   # 342-px posters

# Manual trailer overrides  (tmdb_id : YouTube URL)
MANUAL_TRAILERS = {
    2190: "https://www.youtube.com/watch?v=oUIK01ek-Ko",   # South Park
    1413: "https://www.youtube.com/watch?v=L-WWR7bPvCI",   # American horror Story
}

# ---------- MOVIE helpers ----------------------

# Returns the first matching movie ID or none
@functools.lru_cache(maxsize=128)
def search_movie_id(title: str, year: int | None = None) -> int | None:

    params = {"api_key": API_KEY, "query": title, "include_adult": False}

    if year:

        params["year"] = year

    data = requests.get(f"{BASE}/search/movie", params=params, timeout=7).json()

    res = data.get("results") or []

    return res[0]["id"] if res else None

# Finds full movie details including title, poster, and trailer
@functools.lru_cache(maxsize=64)
def get_movie(mid: int):

    data = requests.get(

        f"{BASE}/movie/{mid}",

        params={"api_key": API_KEY, "append_to_response": "videos"},

        timeout=10,

    ).json()

    # Poster URL (or none)
    poster = data.get("poster_path")

    poster_url  = f"{IMG_CDN}{poster}" if poster else None

    # First YouTube trailer available
    vids = [

        v for v in data.get("videos", {}).get("results", [])

        if v["site"] == "YouTube" and v["type"] == "Trailer"

    ]

    trailer_url = f"https://youtu.be/{vids[0]['key']}" if vids else "#"

    # If no trailer from TMDB, fall back to manual list
    if trailer_url == "#" and mid in MANUAL_TRAILERS:

        trailer_url = MANUAL_TRAILERS[mid]

    return {

        "title":   data["title"],
        "poster":  poster_url,
        "trailer": trailer_url,

    }

# ---------- TV helpers ---------------------------------------

# Returns the first matching TV show ID or none
@functools.lru_cache(maxsize=128)
def search_show_id(name: str, year: int | None = None) -> int | None:

    params = {"api_key": API_KEY, "query": name, "include_adult": False}

    if year:

        params["first_air_date_year"] = year

    data = requests.get(f"{BASE}/search/tv", params=params, timeout=7).json()

    res = data.get("results") or []

    return res[0]["id"] if res else None

# Finds full TV show details including title, poster, and trailer
@functools.lru_cache(maxsize=64)
def get_show(sid: int):

    data = requests.get(

        f"{BASE}/tv/{sid}",
        params={"api_key": API_KEY, "append_to_response": "videos"},
        timeout=10,

    ).json()

    # Poster URL (or none)
    poster = data.get("poster_path")

    poster_url = f"{IMG_CDN}{poster}" if poster else None

    # First YouTube trailer available
    vids = [

        v for v in data.get("videos", {}).get("results", [])

        if v["site"] == "YouTube" and v["type"] == "Trailer"

    ]

    trailer_url = f"https://youtu.be/{vids[0]['key']}" if vids else "#"

    # unconditional manual override (TV shows often lack official trailers)
    if sid in MANUAL_TRAILERS:

        trailer_url = MANUAL_TRAILERS[sid]

    return {"title": data["name"], "poster": poster_url, "trailer": trailer_url}

# ---------- Shared helper ----------------------------------------

# Internal function to help build the title, poster, and trailer dictionaries
def _build_dict(data: dict, *, title_key: str):

    poster = data.get("poster_path")

    poster_url = f"{IMG_CDN}{poster}" if poster else None

    vids = [

        v for v in data.get("videos", {}).get("results", [])

        if v["site"] == "YouTube" and v["type"] == "Trailer"

    ]

    trailer_url = f"https://youtu.be/{vids[0]['key']}" if vids else "#"

    return {"title": data[title_key], "poster": poster_url, "trailer": trailer_url}