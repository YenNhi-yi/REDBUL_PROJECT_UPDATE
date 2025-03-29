from PyQt6.QtWidgets import QMainWindow
from Project.ui.DBSHMainWindow import Ui_MainWindow


class DBSHMainWindowExt(QMainWindow, Ui_MainWindow):
    def __init__(self, on_start_questions):
        super().__init__()
        self.setupUi(self)
        self.on_start_questions = on_start_questions
        self.setup_events()

    def setup_events(self):
        # Gán nút chính (icon nhân vật) để chuyển sang phần câu hỏi
        self.pushButton.clicked.connect(self.handle_start)

    def handle_start(self):
        # Khi người chơi nhấn vào icon → bắt đầu chơi tỉnh trong miền DBSH
        self.on_start_questions("Đồng Bằng Sông Hồng")
