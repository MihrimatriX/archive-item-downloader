import os
from typing import Optional, List
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTextEdit, QFileDialog
)

class TextTab(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.metin_dosya_yolu: Optional[str] = None
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

        text_file_layout: QHBoxLayout = QHBoxLayout()
        self.metin_dosya_label: QLabel = QLabel("Dosya seçilmedi")
        self.metin_dosya_sec: QPushButton = QPushButton("Metin Dosyası Seç")
        self.metin_dosya_sec.clicked.connect(self.metin_dosya_sec_clicked)

        text_file_layout.addWidget(self.metin_dosya_label)
        text_file_layout.addWidget(self.metin_dosya_sec)

        self.metin_editor: QTextEdit = QTextEdit()
        self.metin_editor.setReadOnly(False)

        button_layout: QHBoxLayout = QHBoxLayout()
        self.sirala_buton: QPushButton = QPushButton("Alfabetik Sırala")
        self.sirala_buton.clicked.connect(self.metin_sirala)
        self.tekrar_temizle_buton: QPushButton = QPushButton("Tekrarları Temizle")
        self.tekrar_temizle_buton.clicked.connect(self.tekrarlari_temizle)
        self.kaydet_buton: QPushButton = QPushButton("Kaydet")
        self.kaydet_buton.clicked.connect(self.metin_kaydet)

        button_layout.addWidget(self.sirala_buton)
        button_layout.addWidget(self.tekrar_temizle_buton)
        button_layout.addWidget(self.kaydet_buton)

        layout.addLayout(text_file_layout)
        layout.addWidget(self.metin_editor)
        layout.addLayout(button_layout)

    def metin_dosya_sec_clicked(self) -> None:
        dosya_yolu, _ = QFileDialog.getOpenFileName(
            self,
            "Metin Dosyası Seç",
            "",
            "Text Dosyaları (*.txt);;Tüm Dosyalar (*.*)"
        )

        if dosya_yolu:
            try:
                with open(dosya_yolu, "r", encoding="utf-8") as f:
                    icerik = f.read()
                self.metin_dosya_yolu = dosya_yolu
                self.metin_dosya_label.setText(os.path.basename(dosya_yolu))
                self.metin_editor.setPlainText(icerik)
            except Exception as e:
                self.parent().log_yaz(f"Dosya okuma hatası: {e}", "kirmizi")

    def metin_sirala(self) -> None:
        import locale
        try:
            # Türkçe locale'i ayarla
            locale.setlocale(locale.LC_COLLATE, 'tr_TR.UTF-8')
        except:
            try:
                # Windows için alternatif
                locale.setlocale(locale.LC_COLLATE, 'Turkish_Turkey.1254')
            except:
                pass

        metin = self.metin_editor.toPlainText()
        satirlar = [satir.strip() for satir in metin.splitlines() if satir.strip()]
        
        # Türkçe karakter desteği ile sıralama
        try:
            satirlar.sort(key=locale.strxfrm)
        except:
            # Eğer locale ayarlanamazsa normal sıralama yap
            satirlar.sort()
            
        self.metin_editor.setPlainText("\n".join(satirlar))
        main_window = self.get_main_window()
        if main_window:
            main_window.log_yaz("Metin alfabetik olarak sıralandı.", "normal")

    def tekrarlari_temizle(self) -> None:
        metin = self.metin_editor.toPlainText()
        satirlar = [satir.strip() for satir in metin.splitlines() if satir.strip()]
        benzersiz_satirlar = list(dict.fromkeys(satirlar))
        self.metin_editor.setPlainText("\n".join(benzersiz_satirlar))
        silinen_sayisi = len(satirlar) - len(benzersiz_satirlar)
        main_window = self.get_main_window()
        if main_window:
            main_window.log_yaz(f"{silinen_sayisi} tekrar eden satır temizlendi.", "normal")

    def metin_kaydet(self) -> None:
        try:
            dosya_yolu, _ = QFileDialog.getSaveFileName(
                self,
                "Metni Kaydet",
                "",
                "Text Dosyaları (*.txt);;Tüm Dosyalar (*.*)"
            )

            if dosya_yolu:
                with open(dosya_yolu, "w", encoding="utf-8") as f:
                    f.write(self.metin_editor.toPlainText())
                main_window = self.get_main_window()
                if main_window:
                    main_window.log_yaz("Metin başarıyla kaydedildi!", "normal")
        except Exception as e:
            main_window = self.get_main_window()
            if main_window:
                main_window.log_yaz(f"Dosya kaydetme hatası: {e}", "kirmizi") 