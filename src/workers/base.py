import os
import hashlib
import requests
from typing import List, Optional, Set
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QWidget
from src.api.base import BaseAPI

class BaseDownloaderThread(QThread):
    log_signal: Signal = Signal(str, str)
    finished_signal: Signal = Signal(list)

    def __init__(self, items: List[str], api: BaseAPI, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.items: List[str] = items
        self.api: BaseAPI = api
        self.output_dir: str = ""

    def _create_hash(self, file_path: str) -> str:
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()

    def _download_cover(self, item_name: str, cover_url: str) -> bool:
        try:
            response: requests.Response = requests.get(cover_url)
            if response.status_code == 200:
                file_path: str = os.path.join(self.output_dir, f"{item_name}.jpg")
                with open(file_path, "wb") as f:
                    f.write(response.content)
                return os.path.getsize(file_path) >= 1000
        except Exception:
            return False
        return False 