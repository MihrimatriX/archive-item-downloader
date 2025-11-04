from typing import List, Optional
from PySide6.QtWidgets import QWidget
from src.workers.base import BaseDownloaderThread
from src.api.omdb import OMDbAPI
from src.api.tmdb import TMDBAPI

class FilmDownloaderThread(BaseDownloaderThread):
    def __init__(self, films: List[str], omdb_api: OMDbAPI, tmdb_api: TMDBAPI, parent: Optional[QWidget] = None) -> None:
        super().__init__(films, omdb_api, parent)
        self.tmdb_api = tmdb_api
        self.output_dir: str = "Filmler"

    def run(self) -> None:
        failed_films = []
        self.log_signal.emit("Film kapak indirme işlemi başladı...", "normal")

        for film in self.items:
            try:
                film_id = self.tmdb_api.search(film)
                if film_id:
                    cover_url = self.tmdb_api.get_cover_url(film_id)
                    if cover_url and self._download_cover(film, cover_url):
                        self.log_signal.emit(f"✓ {film} indirildi", "normal")
                        continue

                film_id = self.api.search(film)
                if film_id:
                    cover_url = self.api.get_cover_url(film_id)
                    if cover_url and self._download_cover(film, cover_url):
                        self.log_signal.emit(f"✓ {film} indirildi", "normal")
                        continue

                self.log_signal.emit(f"× {film} için kapak bulunamadı", "kirmizi")
                failed_films.append(film)
            except Exception as e:
                self.log_signal.emit(f"× {film} için hata: {str(e)}", "kirmizi")
                failed_films.append(film)

        self.finished_signal.emit(failed_films) 