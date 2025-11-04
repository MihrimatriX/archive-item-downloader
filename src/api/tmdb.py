import requests
from typing import Optional, Dict, Any
from .base import BaseAPI

class TMDBAPI(BaseAPI):
    def __init__(self, api_key: str) -> None:
        self.api_key: str = api_key
        self.base_url: str = "https://api.themoviedb.org/3"
        self.image_base_url: str = "https://image.tmdb.org/t/p/original"

    def search(self, film_name: str) -> Optional[str]:
        url: str = f"{self.base_url}/search/movie"
        params: Dict[str, str] = {
            "api_key": self.api_key,
            "query": film_name,
            "language": "tr-TR"
        }
        try:
            response: requests.Response = requests.get(url, params=params)
            if response.status_code == 200:
                data: Dict[str, Any] = response.json()
                results: list = data.get("results", [])
                if results:
                    return str(results[0].get("id"))
        except Exception:
            return None
        return None

    def get_cover_url(self, film_id: Optional[str]) -> Optional[str]:
        if not film_id:
            return None
        url: str = f"{self.base_url}/movie/{film_id}"
        params: Dict[str, str] = {
            "api_key": self.api_key,
            "language": "tr-TR"
        }
        try:
            response: requests.Response = requests.get(url, params=params)
            if response.status_code == 200:
                data: Dict[str, Any] = response.json()
                poster_path: str = data.get("poster_path", "")
                if poster_path:
                    return f"{self.image_base_url}{poster_path}"
        except Exception:
            return None
        return None

    def film_adi_cevir(self, film_adi: str) -> Optional[str]:
        url: str = f"{self.base_url}/search/movie"
        params: Dict[str, str] = {
            "api_key": self.api_key,
            "query": film_adi,
            "language": "tr-TR"
        }
        try:
            response: requests.Response = requests.get(url, params=params)
            if response.status_code == 200:
                data: Dict[str, Any] = response.json()
                results: list = data.get("results", [])
                if results:
                    return results[0].get("title")
        except Exception:
            return None
        return None 