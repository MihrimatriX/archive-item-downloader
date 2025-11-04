from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class APIConfig:
    twitch_client_id: str = os.getenv('TWITCH_CLIENT_ID', '')
    twitch_client_secret: str = os.getenv('TWITCH_CLIENT_SECRET', '')
    steam_api_key: str = os.getenv('STEAM_API_KEY', '')
    omdb_api_key: str = os.getenv('OMDB_API_KEY', '')
    tmdb_api_key: str = os.getenv('TMDB_API_KEY', '')