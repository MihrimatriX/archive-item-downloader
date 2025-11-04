from typing import List, Optional
from PySide6.QtWidgets import QWidget
from src.workers.base import BaseDownloaderThread
from src.api.twitch import TwitchAPI
from src.api.steam import SteamAPI
from src.api.epic import EpicAPI

class GameDownloaderThread(BaseDownloaderThread):
    def __init__(self, games: List[str], twitch_api: TwitchAPI, steam_api: SteamAPI, epic_api: EpicAPI, parent: Optional[QWidget] = None) -> None:
        super().__init__(games, twitch_api, parent)
        self.twitch_api: TwitchAPI = twitch_api
        self.steam_api: SteamAPI = steam_api
        self.epic_api: EpicAPI = epic_api
        self.output_dir: str = "Oyunlar"

    def run(self) -> None:
        failed_items: List[str] = []
        self.log_signal.emit("Oyun kapak indirme işlemi başladı...", "normal")

        for game_name in self.items:
            try:
                game_id = self.twitch_api.search(game_name)
                if game_id:
                    cover_url = self.twitch_api.get_cover_url(game_id)
                    if cover_url and self._download_cover(game_name, cover_url):
                        self.log_signal.emit(f"✓ {game_name} indirildi (Twitch)", "normal")
                        continue

                self.log_signal.emit(f"Twitch'te bulunamadı, Steam deneniyor: {game_name}", "normal")
                game_id = self.steam_api.search(game_name)
                if game_id:
                    cover_url = self.steam_api.get_cover_url(game_id)
                    if cover_url and self._download_cover(game_name, cover_url):
                        self.log_signal.emit(f"✓ {game_name} indirildi (Steam)", "normal")
                        continue

                self.log_signal.emit(f"Steam'de bulunamadı, Epic Store deneniyor: {game_name}", "normal")
                game_id = self.epic_api.search(game_name)
                if game_id:
                    cover_url = self.epic_api.get_cover_url(game_id)
                    if cover_url and self._download_cover(game_name, cover_url):
                        self.log_signal.emit(f"✓ {game_name} indirildi (Epic)", "normal")
                        continue

                self.log_signal.emit(f"× {game_name} için kapak bulunamadı", "kirmizi")
                failed_items.append(game_name)

            except Exception as e:
                self.log_signal.emit(f"× {game_name} için hata: {str(e)}", "kirmizi")
                failed_items.append(game_name)

        self.finished_signal.emit(failed_items)