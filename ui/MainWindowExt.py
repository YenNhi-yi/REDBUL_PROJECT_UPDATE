from PyQt6.QtWidgets import QMainWindow

from Project.ui.MainWindow import Ui_MainWindow
from Project.ui.Top10MainWindowExt import Top10MainWindow


class MainWindowExt(QMainWindow, Ui_MainWindow):
    def __init__(self, username=None, auth=None, on_play_clicked=None):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.auth = auth
        self.on_play_clicked = on_play_clicked
        self.setup_events()
        self.top10_window = None  # ➕ Biến để lưu cửa sổ Top10

    def setup_events(self):
        self.pushButton.clicked.connect(self.start_game)
        self.pushButton_Top10.clicked.connect(self.show_top10_window)  # ➕ Gán sự kiện nút TOP10

    def start_game(self):
        print(f"Người chơi {self.username} bắt đầu khám phá!")
        print(f"[DEBUG] current_player trong MainWindowExt: {self.auth.get_current_player()}")
        if self.on_play_clicked:
            self.on_play_clicked()

    def show_top10_window(self):
        self.top10_window = Top10MainWindow()
        self.top10_window.show()
