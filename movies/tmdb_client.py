# movies/tmdb_client.py
import os, requests, functools

API_KEY = os.getenv("TMDB_API_KEY")            # already loaded from .env
BASE    = "https://api.themoviedb.org/3"
IMG_CDN = "https://image.tmdb.org/t/p/w342"   # 342-px posters

@functools.lru_cache(maxsize=128)
def search_id(title: str, year: int | None = None) -> int | None:
    """Return TMDB movie-id for a title+year (first hit) or None."""
    params = {"api_key": API_KEY, "query": title, "include_adult": False}
    if year:
        params["year"] = year
    data = requests.get(f"{BASE}/search/movie", params=params, timeout=7).json()
    results = data.get("results") or []
    return results[0]["id"] if results else None


@functools.lru_cache(maxsize=64)
def get_movie(mid: int):
    """Return {title, poster, trailer} for a TMDB movie-id."""
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

    return {"title": data["title"], "poster": poster_url, "trailer": trailer_url}