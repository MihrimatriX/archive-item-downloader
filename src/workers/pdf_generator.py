import os
import math
from typing import List, Optional
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QWidget
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from PIL import Image

class PDFGenerator(QThread):
    log_signal: Signal = Signal(str, str)
    finished_signal: Signal = Signal()

    def __init__(self, image_list: List[str], parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.image_list: List[str] = image_list
        self.long_edge: float = 15 * cm
        self.short_edge: float = 11 * cm
        self.margin: float = 2 * cm
        self.padding: float = 0 * cm

    def run(self) -> None:
        try:
            pdf_file: str = "resimler.pdf"
            c: canvas.Canvas = canvas.Canvas(pdf_file, pagesize=A4)
            page_width, page_height = A4

            usable_width: float = page_width - (2 * self.margin)
            usable_height: float = page_height - (2 * self.margin)

            horizontal_count: int = max(1, math.floor(usable_width / self.long_edge))
            vertical_count: int = max(1, math.floor(usable_height / self.short_edge))
            images_per_page: int = horizontal_count * vertical_count

            for i, image_path in enumerate(self.image_list):
                try:
                    img: Image.Image = Image.open(image_path)
                    if img.height > img.width:
                        img = img.rotate(90, expand=True)

                    temp_path: str = f"temp_{i}.png"
                    img.save(temp_path, "PNG", optimize=False)

                    if i % images_per_page == 0 and i > 0:
                        c.showPage()

                    x: float = self.margin + (i % horizontal_count) * self.long_edge
                    y: float = page_height - self.margin - ((i % images_per_page) // horizontal_count + 1) * self.short_edge

                    c.drawImage(
                        temp_path,
                        x, y,
                        width=self.long_edge,
                        height=self.short_edge,
                        preserveAspectRatio=False,
                        mask='auto'
                    )

                    os.remove(temp_path)
                    self.log_signal.emit(f"✓ {os.path.basename(image_path)} eklendi", "normal")

                except Exception as e:
                    self.log_signal.emit(f"× {os.path.basename(image_path)} eklenemedi: {str(e)}", "kirmizi")
                    continue

            c.save()
            self.log_signal.emit("PDF başarıyla oluşturuldu!", "normal")
            self.finished_signal.emit()

        except Exception as e:
            self.log_signal.emit(f"PDF oluşturma hatası: {str(e)}", "kirmizi")
            self.finished_signal.emit()