from PyQt6.QtWidgets import QMainWindow, QMessageBox
from Project.ui.SignInMainWinDow import Ui_MainWindow


class SignInMainWinDowExt(QMainWindow):
    def __init__(self, on_login_success, auth):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.auth=auth

        self.on_login_success = on_login_success

        self.setup_events()

    def setup_events(self):
        self.ui.pushButton_DangNhap.clicked.connect(self.handle_login)
        self.ui.pushButton_DangKy.clicked.connect(self.handle_register)

    def handle_login(self):
        username = self.ui.lineEdit_DNusername.text().strip()
        password = self.ui.lineEdit_DNpassword.text().strip()

        if self.auth.login(username, password):
            self.clearFocus()

            if username == "nhi":
                from Project.ui.Admin_MainWindowExt import Admin_MainWindowExt
                self.admin_window = Admin_MainWindowExt()
                self.admin_window.show()
                self.close()

            else:
                self.on_login_success(username)
                self.close()
        else:
            QMessageBox.warning(self, "Thất bại", "Tên người dùng hoặc mật khẩu không đúng.")

    def handle_register(self):
        username = self.ui.lineEdit_DKusername.text().strip()
        password = self.ui.lineEdit_DKpassword1.text().strip()
        confirm = self.ui.lineEdit_DKpassword2.text().strip()

        try:
            success, message = self.auth.register(username, password, confirm)
            if success:
                QMessageBox.information(self, "Đăng ký thành công", message)
            else:
                QMessageBox.warning(self, "Thất bại", message)
        except Exception as e:
            QMessageBox.critical(self, "Lỗi nghiêm trọng", f"Đăng ký thất bại:\n{str(e)}")
