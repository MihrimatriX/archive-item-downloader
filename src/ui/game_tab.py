from typing import Optional
import os
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QListWidget, QFileDialog, QListWidgetItem
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from src.workers.game_downloader import GameDownloaderThread
from src.api.twitch import TwitchAPI
from src.api.steam import SteamAPI
from src.api.epic import EpicAPI

class GameTab(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.oyun_dosya_yolu: Optional[str] = None
        self._setup_ui()

    def get_main_window(self):
        parent = self.parent()
        while parent is not None:
            if hasattr(parent, "config"):
                return parent
            parent = parent.parent()
        return None

    def _setup_ui(self) -> None:
        layout: QVBoxLayout = QVBoxLayout(self)

        file_layout: QHBoxLayout = QHBoxLayout()
        self.dosya_label: QLabel = QLabel("Dosya seçilmedi")
        self.dosya_sec: QPushButton = QPushButton("Oyun Listesi Seç")
        self.dosya_sec.clicked.connect(self.dosya_sec_clicked)

        file_layout.addWidget(self.dosya_label)
        file_layout.addWidget(self.dosya_sec)

        self.list_widget: QListWidget = QListWidget()
        self.buton_indir: QPushButton = QPushButton("Oyun Kapaklarını İndir")
        self.buton_indir.clicked.connect(self.oyunlari_indir)

        layout.addLayout(file_layout)
        layout.addWidget(self.list_widget)
        layout.addWidget(self.buton_indir)

    def dosya_sec_clicked(self) -> None:
        dosya_yolu, _ = QFileDialog.getOpenFileName(
            self,
            "Oyun Listesi Seç",
            "",
            "Text Dosyaları (*.txt);;Tüm Dosyalar (*.*)"
        )

        if dosya_yolu:
            try:
                with open(dosya_yolu, "r", encoding="utf-8") as f:
                    satirlar = [satir.strip() for satir in f if satir.strip()]

                self.oyun_dosya_yolu = dosya_yolu
                self.dosya_label.setText(os.path.basename(dosya_yolu))
                self.list_widget.clear()
                for satir in satirlar:
                    item = QListWidgetItem(f"⏳ {satir}")
                    item.setData(Qt.UserRole, satir)
                    self.list_widget.addItem(item)
            except Exception as e:
                main_window = self.get_main_window()
                if main_window:
                    main_window.log_yaz(f"Dosya okuma hatası: {e}", "kirmizi")

    def oyunlari_indir(self) -> None:
        if not self.oyun_dosya_yolu:
            main_window = self.get_main_window()
            if main_window:
                main_window.log_yaz("Lütfen önce bir oyun listesi seçin!", "kirmizi")
            return

        try:
            with open(self.oyun_dosya_yolu, "r", encoding="utf-8") as f:
                oyunlar = [satir.strip() for satir in f if satir.strip()]
        except Exception as e:
            main_window = self.get_main_window()
            if main_window:
                main_window.log_yaz(f"Hata: {e}", "kirmizi")
            return

        os.makedirs("Oyunlar", exist_ok=True)

        main_window = self.get_main_window()
        if main_window:
            config = main_window.config
            self.game_thread = GameDownloaderThread(
                oyunlar,
                TwitchAPI(config.twitch_client_id, config.twitch_client_secret),
                SteamAPI(config.steam_api_key),
                EpicAPI()
            )
            self.game_thread.log_signal.connect(lambda msg, t: main_window.log_yaz(msg, t))
            self.game_thread.log_signal.connect(self.oyun_durum_guncelle)
            self.game_thread.finished_signal.connect(self.oyunlar_bitti)
            self.game_thread.start()

    def oyunlar_bitti(self, failed: list) -> None:
        if failed:
            with open("failed_games.txt", "w", encoding="utf-8") as f:
                for oyun in failed:
                    f.write(oyun + "\n")
            main_window = self.get_main_window()
            if main_window:
                main_window.log_yaz("Bazı oyunlar indirilemedi. failed_games.txt dosyasına yazıldı.", "kirmizi")

    def oyun_durum_guncelle(self, mesaj: str, tur: str) -> None:
        if mesaj.startswith("✓"):
            oyun_adi = mesaj[2:].split(" indirildi")[0]
            self.liste_ozet_guncelle(oyun_adi, True)
        elif mesaj.startswith("×"):
            oyun_adi = mesaj[2:].split(" için")[0].split(" hata")[0]
            self.liste_ozet_guncelle(oyun_adi, False)

    def liste_ozet_guncelle(self, isim: str, basarili: bool) -> None:
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            if item.data(Qt.UserRole) == isim:
                if basarili:
                    item.setText(f"✅ {isim}")
                    item.setForeground(QColor("#4CAF50"))
                else:
                    item.setText(f"❌ {isim}")
                    item.setForeground(QColor("#F44336"))
                break