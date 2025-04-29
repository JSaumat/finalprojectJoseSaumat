# movies/tmdb_client.py
import os, requests, functools

API_KEY = os.getenv("TMDB_API_KEY")            # already loaded from .env
BASE    = "https://api.themoviedb.org/3"
IMG_CDN = "https://image.tmdb.org/t/p/w342"   # 342-px posters

# Manual trailer overrides  (tmdb_id : YouTube URL)
MANUAL_TRAILERS = {
    2190: "https://www.youtube.com/watch?v=oUIK01ek-Ko",   # South Park
    1413: "https://www.youtube.com/watch?v=L-WWR7bPvCI",   # American horror Story
}

# ---------- MOVIE helpers ----------------------

@functools.lru_cache(maxsize=128)
def search_movie_id(title: str, year: int | None = None) -> int | None:
    params = {"api_key": API_KEY, "query": title, "include_adult": False}
    if year:
        params["year"] = year
    data = requests.get(f"{BASE}/search/movie", params=params, timeout=7).json()
    res = data.get("results") or []
    return res[0]["id"] if res else None


@functools.lru_cache(maxsize=64)
def get_movie(mid: int):
    data = requests.get(
        f"{BASE}/movie/{mid}",
        params={"api_key": API_KEY, "append_to_response": "videos"},
        timeout=10,
    ).json()

    poster = data.get("poster_path")
    poster_url  = f"{IMG_CDN}{poster}" if poster else None

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

@functools.lru_cache(maxsize=128)
def search_show_id(name: str, year: int | None = None) -> int | None:
    params = {"api_key": API_KEY, "query": name, "include_adult": False}
    if year:
        params["first_air_date_year"] = year
    data = requests.get(f"{BASE}/search/tv", params=params, timeout=7).json()
    res = data.get("results") or []
    return res[0]["id"] if res else None


@functools.lru_cache(maxsize=64)
def get_show(sid: int):
    data = requests.get(
        f"{BASE}/tv/{sid}",
        params={"api_key": API_KEY, "append_to_response": "videos"},
        timeout=10,
    ).json()

    poster = data.get("poster_path")
    poster_url = f"{IMG_CDN}{poster}" if poster else None

    vids = [
        v for v in data.get("videos", {}).get("results", [])
        if v["site"] == "YouTube" and v["type"] == "Trailer"
    ]
    trailer_url = f"https://youtu.be/{vids[0]['key']}" if vids else "#"

    # ── unconditional manual override if present ──
    if sid in MANUAL_TRAILERS:
        trailer_url = MANUAL_TRAILERS[sid]

    return {"title": data["name"], "poster": poster_url, "trailer": trailer_url}

# ---------- Shared helper ----------------------------------------

def _build_dict(data: dict, *, title_key: str):
    poster = data.get("poster_path")
    poster_url = f"{IMG_CDN}{poster}" if poster else None

    vids = [
        v for v in data.get("videos", {}).get("results", [])
        if v["site"] == "YouTube" and v["type"] == "Trailer"
    ]
    trailer_url = f"https://youtu.be/{vids[0]['key']}" if vids else "#"

    return {"title": data[title_key], "poster": poster_url, "trailer": trailer_url}