import requests
from typing import Optional, Dict, Any
from .base import BaseAPI

class OMDbAPI(BaseAPI):
    def __init__(self, api_key: str) -> None:
        self.api_key: str = api_key

    def search(self, film_name: str) -> Optional[str]:
        url: str = f"http://www.omdbapi.com/?t={film_name}&apikey={self.api_key}"
        try:
            response: requests.Response = requests.get(url)
            if response.status_code == 200:
                data: Dict[str, Any] = response.json()
                return data.get("Title") if data.get("Response") == "True" else None
        except Exception:
            return None
        return None

    def get_cover_url(self, film_id: Optional[str]) -> Optional[str]:
        if not film_id:
            return None
        url: str = f"http://www.omdbapi.com/?t={film_id}&apikey={self.api_key}"
        try:
            response: requests.Response = requests.get(url)
            if response.status_code == 200:
                data: Dict[str, Any] = response.json()
                if data.get("Response") == "True":
                    poster_url: str = data.get("Poster", "")
                    return poster_url if poster_url != "N/A" else None
        except Exception:
            return None
        return None

    def film_adi_cevir(self, film_adi: str) -> Optional[str]:
        url: str = f"http://www.omdbapi.com/?t={film_adi}&apikey={self.api_key}"
        try:
            response: requests.Response = requests.get(url)
            if response.status_code == 200:
                data: Dict[str, Any] = response.json()
                if data.get("Response") == "True":
                    return data.get("Title")
        except Exception:
            return None
        return None 