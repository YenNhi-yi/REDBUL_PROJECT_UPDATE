from PyQt6.QtWidgets import QApplication, QMessageBox

from Project.Controllers.AuthController import AuthController
from Project.Controllers.GameController import GameController
from Project.ui.GD8MienMainWindowExt import GD8MienMainWindowExt
from Project.ui.MainWindowExt import MainWindowExt
from Project.ui.SignInMainWindowExt import SignInMainWinDowExt
from Project.ui.TBBMainWindowExt import TBBMainWindowExt
from Project.ui_DBB.DBBMainWindowExt import DBBMainWindowExt


class GameApp:
    def __init__(self):
        self.app = QApplication([])
        self.auth = AuthController()

        self.show_sign_in()

    def show_sign_in(self):
        self.sign_in_window = SignInMainWinDowExt(self.handle_login_success, auth=self.auth)
        self.sign_in_window.show()
        self.app.exec()

    def handle_login_success(self, username):
        print(f"Người chơi {username} bắt đầu khám phá!")
        self.controller = GameController(auth=self.auth)
        self.show_main_window()
        self.sign_in_window.close()

    def show_main_window(self):
        self.main_window = MainWindowExt(on_play_clicked=self.show_region_selection, auth=self.auth)
        self.main_window.show()
        self.sign_in_window.close()

    def show_region_selection(self):
        self.region_window = GD8MienMainWindowExt(on_region_selected=self.start_question_play, auth=self.auth)
        self.region_window.show()
        self.main_window.close()

    def start_question_play(self, region_name):
        print(f"Bạn đã chọn miền: {region_name}")

        region_map = {
            "TayBacBo": TBBMainWindowExt,
            "DongBacBo": DBBMainWindowExt,
            # Thêm các miền khác ở đây nếu cần
        }

        region_cls = region_map.get(region_name)
        if region_cls:
            self.region_main = region_cls(on_start_questions=self.show_region_selection, auth=self.auth)
            self.region_main.show()
        else:
            QMessageBox.information(None, "Thông báo", f"Miền {region_name} chưa được triển khai.")


if __name__ == "__main__":
    game = GameApp()
