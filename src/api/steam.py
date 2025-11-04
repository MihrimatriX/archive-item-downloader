import requests
from typing import Optional, Dict, Any, List
from .base import BaseAPI

class SteamAPI(BaseAPI):
    def __init__(self, api_key: str) -> None:
        self.api_key: str = api_key
        self.base_url: str = "https://api.steampowered.com/ISteamApps/GetAppList/v2"
        self.search_url: str = "https://store.steampowered.com/api/storesearch"
        self._app_list_cache: Optional[List[Dict[str, Any]]] = None
        self._load_app_list()

    def _load_app_list(self) -> None:
        try:
            response: requests.Response = requests.get(self.base_url)
            if response.status_code == 200:
                data: Dict[str, Any] = response.json()
                self._app_list_cache = data.get("applist", {}).get("apps", [])
        except Exception as e:
            print(f"Steam API yükleme hatası: {e}")
            self._app_list_cache = []

    def _clean_game_name(self, game_name: str) -> str:
        tr_chars = {'ı': 'i', 'ğ': 'g', 'ü': 'u', 'ş': 's', 'ö': 'o', 'ç': 'c', 'İ': 'I', 'Ğ': 'G', 'Ü': 'U', 'Ş': 'S', 'Ö': 'O', 'Ç': 'C'}
        for tr_char, eng_char in tr_chars.items():
            game_name = game_name.replace(tr_char, eng_char)
        return ''.join(c.lower() for c in game_name if c.isalnum() or c.isspace())

    def search(self, game_name: str) -> Optional[str]:
        try:
            params: Dict[str, str] = {
                "term": game_name,
                "cc": "tr",
                "l": "turkish"
            }
            response: requests.Response = requests.get(self.search_url, params=params)
            if response.status_code == 200:
                data: Dict[str, Any] = response.json()
                items: List[Dict[str, Any]] = data.get("items", [])
                if items:
                    return str(items[0].get("id"))
        except Exception as e:
            print(f"Steam API arama hatası: {e}")
        return None

    def get_cover_url(self, game_id: Optional[str]) -> Optional[str]:
        if not game_id:
            return None
        url = f"https://cdn.akamai.steamstatic.com/steam/apps/{game_id}/library_600x900.jpg"
        try:
            response: requests.Response = requests.head(url)
            return url if response.status_code == 200 else None
        except Exception:
            return None