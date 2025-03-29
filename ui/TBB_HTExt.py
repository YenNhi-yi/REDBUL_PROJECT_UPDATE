from PyQt6.QtWidgets import QMainWindow
from Project.ui.TBB_HT import Ui_MainWindow


class TBB_HTExt(QMainWindow, Ui_MainWindow):
    def __init__(self, parent_to_close=None):
        super().__init__()
        self.setupUi(self)
        self.parent_to_close = parent_to_close

        self.pushButton_Next.clicked.connect(self.go_to_mien_screen)

    def go_to_mien_screen(self):
        # Đóng giao diện hiện tại và giao diện câu hỏi (nếu có)
        if self.parent_to_close:
            self.parent_to_close.close()
        self.close()

        from Project.ui.GD8MienMainWindowExt import GD8MienMainWindowExt

        # Mở giao diện chọn miền
        self.mien_window = GD8MienMainWindowExt(on_region_selected=self.region_selected)
        self.mien_window.show()

    def region_selected(self, region_name):
        print(f"[TBB_HTExt] Người chơi đã chọn miền: {region_name}")
