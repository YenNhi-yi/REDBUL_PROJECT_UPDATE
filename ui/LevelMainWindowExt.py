from PyQt6.QtWidgets import QMainWindow

from Project.Controllers.AuthController import AuthController
from Project.ui.LevelMainWindow import Ui_MainWindow
from Project.ui.QSTBBMainWindowExt import QSTBBMainWindowExt

class LevelMainWindowExt(QMainWindow, Ui_MainWindow):
    def __init__(self, province_name, current_player, auth=None):
        super().__init__()
        self.setupUi(self)

        self.province_name = province_name         # Tên tỉnh hiện tại
        self.current_player = current_player       # Người chơi đang đăng nhập
        self.auth = auth or AuthController()       # Dùng Auth hiện có, hoặc tạo mới

        self.setup_events()

    def setup_events(self):
        self.pushButton_Easy.clicked.connect(self.start_easy_level)
        self.pushButton_Hard.clicked.connect(self.start_hard_level)

    def start_easy_level(self):
        self.start_game(level="Easy")

    def start_hard_level(self):
        self.start_game(level="Hard")

    def start_game(self, level):
        self.qs_window = QSTBBMainWindowExt(
            province_name=self.province_name,
            level=level,
            current_player=self.current_player,
            auth=self.auth
        )
        self.qs_window.show()
        self.close()
