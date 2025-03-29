import os

from PIL.ImageQt import QPixmap
from PyQt6.QtWidgets import QMainWindow

from Project.ui.Correct import Ui_MainWindow


class CorrectExt(QMainWindow, Ui_MainWindow):
    def __init__(self, image_path="", on_next_callback=None):
        super().__init__()
        self.setupUi(self)
        self.on_next_callback = on_next_callback

        if image_path and os.path.exists(image_path):
            self.label_2.setPixmap(QPixmap(image_path))
            self.label_2.setScaledContents(True)
        else:
            print("[⚠] Không tìm thấy ảnh thẻ:", image_path)

        self.pushButton_Next.clicked.connect(self.handle_next)

    def handle_next(self):
        if self.on_next_callback:
            self.on_next_callback()
        self.close()
