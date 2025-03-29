from PyQt6.QtWidgets import QMainWindow

from Project.Controllers.AuthController import AuthController
from Project.Controllers.RegionController import RegionController
from Project.ui.LevelMainWindowExt import LevelMainWindowExt
from Project.ui.TBBMainWindow import Ui_MainWindow


class TBBMainWindowExt(QMainWindow, Ui_MainWindow):
    def __init__(self, on_start_questions):
        super().__init__()
        self.setupUi(self)

        self.on_start_questions = on_start_questions
        self.auth = AuthController()
        self.player = self.auth.get_current_player()

        self.region_ctrl = RegionController(self.player)

        self.setupSignalAndSlot()

    def setupSignalAndSlot(self):
        self.pushButton.clicked.connect(self.start_level)

    def start_level(self):
        province = self.region_ctrl.get_current_province()
        print(f"[DEBUG] Province hiện tại: {province}")  # ✅ Debug kiểm tra
        if not province:
            print("[LỖI] Không lấy được province từ RegionController")
            return

        self.level_window = LevelMainWindowExt(
            province_name=province,
            current_player=self.player,
            auth=self.auth
        )
        self.level_window.show()
        self.close()
