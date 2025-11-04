import requests
from typing import Optional
from .base import BaseAPI
import re

class EpicAPI(BaseAPI):
    def __init__(self) -> None:
        self.base_url: str = "https://store.epicgames.com/graphql"
        self.search_url: str = "https://store.epicgames.com/en-US/browse"

    def search(self, game_name: str) -> Optional[str]:
        try:
            response = requests.get(
                self.search_url,
                params={"q": game_name},
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
                }
            )

            if response.status_code == 200:
                pattern = r'data-product-id="([^"]+)"'
                matches = re.findall(pattern, response.text)
                if matches:
                    return matches[0]
        except Exception:
            return None
        return None

    def get_cover_url(self, game_id: Optional[str]) -> Optional[str]:
        if not game_id:
            return None

        try:
            query = """
            query getGameDetails($productId: String!) {
                Product {
                    getProduct(productId: $productId) {
                        keyImages {
                            type
                            url
                        }
                    }
                }
            }
            """

            variables = {
                "productId": game_id
            }

            response = requests.post(
                self.base_url,
                json={
                    "query": query,
                    "variables": variables
                },
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
                }
            )

            if response.status_code == 200:
                data = response.json()
                images = data.get("data", {}).get("Product", {}).get("getProduct", {}).get("keyImages", [])

                for image in images:
                    if image.get("type") == "DieselStoreFrontTall":
                        return image.get("url")

                if images:
                    return images[0].get("url")

        except Exception:
            return None
        return None 