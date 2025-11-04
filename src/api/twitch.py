import requests
from typing import Optional, Dict, List
from .base import BaseAPI

class TwitchAPI(BaseAPI):
    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id: str = client_id
        self.client_secret: str = client_secret
        self.token: Optional[str] = self._get_token()

    def _get_token(self) -> Optional[str]:
        url: str = "https://id.twitch.tv/oauth2/token"
        params: Dict[str, str] = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }
        try:
            resp: requests.Response = requests.post(url, params=params)
            return resp.json()["access_token"] if resp.status_code == 200 else None
        except Exception:
            return None

    def search(self, game_name: str) -> Optional[str]:
        if not self.token:
            return None
        headers: Dict[str, str] = {
            "Client-ID": self.client_id,
            "Authorization": f"Bearer {self.token}"
        }
        try:
            response: requests.Response = requests.get(
                "https://api.twitch.tv/helix/search/categories",
                headers=headers,
                params={"query": game_name, "first": 1}
            )
            data: List[Dict[str, str]] = response.json()["data"]
            return data[0]["id"] if data else None
        except Exception:
            return None

    def get_cover_url(self, game_id: Optional[str]) -> Optional[str]:
        return f"https://static-cdn.jtvnw.net/ttv-boxart/{game_id}-285x380.jpg" if game_id else None 