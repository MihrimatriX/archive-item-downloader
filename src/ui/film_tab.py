from typing import Optional
import os
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QListWidget, QFileDialog, QListWidgetItem
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from src.workers.film_downloader import FilmDownloaderThread
from src.api.omdb import OMDbAPI
from src.api.tmdb import TMDBAPI

class FilmTab(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.film_dosya_yolu: Optional[str] = None
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
        self.dosya_sec: QPushButton = QPushButton("Film Listesi Seç")
        self.dosya_sec.clicked.connect(self.dosya_sec_clicked)

        file_layout.addWidget(self.dosya_label)
        file_layout.addWidget(self.dosya_sec)

        self.list_widget: QListWidget = QListWidget()
        self.buton_indir: QPushButton = QPushButton("Film Kapaklarını İndir")
        self.buton_indir.clicked.connect(self.filmleri_indir)
        self.buton_cevir: QPushButton = QPushButton("İngilizce İsimlerle Değiştir")
        self.buton_cevir.clicked.connect(self.film_isimlerini_ingilizce_yap)

        layout.addLayout(file_layout)
        layout.addWidget(self.list_widget)
        layout.addWidget(self.buton_indir)
        layout.addWidget(self.buton_cevir)

    def dosya_sec_clicked(self) -> None:
        dosya_yolu, _ = QFileDialog.getOpenFileName(
            self,
            "Film Listesi Seç",
            "",
            "Text Dosyaları (*.txt);;Tüm Dosyalar (*.*)"
        )

        if dosya_yolu:
            try:
                with open(dosya_yolu, "r", encoding="utf-8") as f:
                    satirlar = [satir.strip() for satir in f if satir.strip()]

                self.film_dosya_yolu = dosya_yolu
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

    def filmleri_indir(self) -> None:
        if not self.film_dosya_yolu:
            main_window = self.get_main_window()
            if main_window:
                main_window.log_yaz("Lütfen önce bir film listesi seçin!", "kirmizi")
            return

        try:
            filmler = []
            for i in range(self.list_widget.count()):
                item = self.list_widget.item(i)
                ing_adi = item.data(Qt.UserRole)
                filmler.append(ing_adi)
        except Exception as e:
            main_window = self.get_main_window()
            if main_window:
                main_window.log_yaz(f"Hata: {e}", "kirmizi")
            return

        os.makedirs("Filmler", exist_ok=True)

        main_window = self.get_main_window()
        if main_window:
            config = main_window.config
            self.film_thread = FilmDownloaderThread(
                filmler,
                OMDbAPI(config.omdb_api_key),
                TMDBAPI(config.tmdb_api_key)
            )
            self.film_thread.log_signal.connect(lambda msg, t: main_window.log_yaz(msg, t))
            self.film_thread.log_signal.connect(self.film_durum_guncelle)
            self.film_thread.finished_signal.connect(self.filmler_bitti)
            self.film_thread.start()

    def filmler_bitti(self, failed: list) -> None:
        if failed:
            with open("failed_films.txt", "w", encoding="utf-8") as f:
                for film in failed:
                    f.write(film + "\n")
            main_window = self.get_main_window()
            if main_window:
                main_window.log_yaz("Bazı filmler indirilemedi. failed_films.txt dosyasına yazıldı.", "kirmizi")

    def film_durum_guncelle(self, mesaj: str, tur: str) -> None:
        if mesaj.startswith("✓"):
            film_adi = mesaj[2:].split(" indirildi")[0]
            self.liste_ozet_guncelle(film_adi, True)
        elif mesaj.startswith("×"):
            film_adi = mesaj[2:].split(" için")[0].split(" hata")[0]
            self.liste_ozet_guncelle(film_adi, False)

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

    def film_isimlerini_ingilizce_yap(self) -> None:
        try:
            from film_cevir import film_eslestirmeleri
        except ImportError:
            main_window = self.get_main_window()
            if main_window:
                main_window.log_yaz("film_cevir.py bulunamadı veya hatalı!", "kirmizi")
            return

        eslestirmeler = film_eslestirmeleri()
        yeni_satirlar = []
        main_window = self.get_main_window()
        if main_window:
            config = main_window.config
            omdb_api = OMDbAPI(config.omdb_api_key)
            tmdb_api = TMDBAPI(config.tmdb_api_key)

            for i in range(self.list_widget.count()):
                item = self.list_widget.item(i)
                turkce_adi = item.data(Qt.UserRole)
                if turkce_adi in eslestirmeler:
                    ing_adi = eslestirmeler[turkce_adi]
                    item.setText(f"🌍 {ing_adi}")
                    item.setData(Qt.UserRole, ing_adi)
                    yeni_satirlar.append(ing_adi)
                    continue

                try:
                    ing_adi = tmdb_api.film_adi_cevir(turkce_adi)
                    if not ing_adi:
                        ing_adi = omdb_api.film_adi_cevir(turkce_adi)

                    if ing_adi:
                        item.setText(f"🌍 {ing_adi}")
                        item.setData(Qt.UserRole, ing_adi)
                        yeni_satirlar.append(ing_adi)
                    else:
                        yeni_satirlar.append(turkce_adi)
                except Exception as e:
                    main_window.log_yaz(f"API hatası ({turkce_adi}): {e}", "kirmizi")
                    yeni_satirlar.append(turkce_adi)

            try:
                with open("FilmList_English.txt", "w", encoding="utf-8") as f:
                    for isim in yeni_satirlar:
                        f.write(isim + "\n")
                main_window.log_yaz("İngilizce film isimleri FilmList_English.txt dosyasına kaydedildi.", "normal")
            except Exception as e:
                main_window.log_yaz(f"Kaydetme hatası: {e}", "kirmizi")

            main_window.log_yaz("Film isimleri İngilizce karşılıklarıyla değiştirildi.", "normal") 