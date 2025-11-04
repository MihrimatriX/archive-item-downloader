from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout,
    QTextEdit, QLabel, QTabWidget, QSplitter
)
from PySide6.QtCore import Qt
from src.ui.game_tab import GameTab
from src.ui.film_tab import FilmTab
from src.ui.pdf_tab import PDFTab
from src.ui.text_tab import TextTab
from src.utils.config import APIConfig

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.config = APIConfig()
        self.setWindowTitle("Kapak İndirici")
        self.setFixedSize(900, 600)
        self._setup_ui()

    def _setup_ui(self) -> None:
        self.setStyleSheet("""
            QMainWindow {
                background-color: #121212;
                color: white;
            }
            QPushButton {
                background-color: #2d2d2d;
                color: white;
                border: 1px solid #3d3d3d;
                padding: 8px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #3d3d3d;
            }
            QTextEdit, QListWidget {
                background-color: #1e1e1e;
                color: white;
                border: 1px solid #3d3d3d;
                border-radius: 4px;
            }
            QLabel {
                color: white;
            }
            QTabWidget::pane {
                border: 1px solid #3d3d3d;
                border-radius: 4px;
            }
            QTabBar::tab {
                background-color: #2d2d2d;
                color: white;
                padding: 8px 16px;
                border: 1px solid #3d3d3d;
                border-bottom: none;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            QTabBar::tab:selected {
                background-color: #3d3d3d;
            }
            QSpinBox {
                background-color: #2d2d2d;
                color: white;
                border: 1px solid #3d3d3d;
                padding: 4px;
                border-radius: 4px;
            }
        """)

        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        splitter = QSplitter()
        splitter.setOrientation(Qt.Vertical)

        tab_widget = QTabWidget()
        tab_widget.addTab(GameTab(self), "Oyunlar")
        tab_widget.addTab(FilmTab(self), "Filmler")
        tab_widget.addTab(PDFTab(self), "PDF Oluşturucu")
        tab_widget.addTab(TextTab(self), "Metin Düzenleyici")

        log_widget = QWidget()
        log_layout = QVBoxLayout(log_widget)
        log_layout.addWidget(QLabel("Log Paneli:"))
        self.text_log = QTextEdit()
        self.text_log.setReadOnly(True)
        log_layout.addWidget(self.text_log)

        splitter.addWidget(tab_widget)
        splitter.addWidget(log_widget)
        splitter.setSizes([400, 200])

        main_layout.addWidget(splitter)
        self.setCentralWidget(main_widget)

    def log_yaz(self, mesaj: str, tur: str = "normal") -> None:
        if tur == "hata":
            self.text_log.append(f'<span style="color: red;">{mesaj}</span>')
        elif tur == "basarili":
            self.text_log.append(f'<span style="color: green;">{mesaj}</span>')
        else:
            self.text_log.append(mesaj) 