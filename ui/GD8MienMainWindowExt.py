from PyQt6 import QtWidgets, QtGui, QtCore
import os

from Project.ui.GD8MienMainWindow import Ui_MainWindow
from Project.ui.TBBMainWindowExt import TBBMainWindowExt
from Project.ui_DBB.DBBMainWindowExt import DBBMainWindowExt


class GD8MienMainWindowExt(QtWidgets.QMainWindow):
    def __init__(self, on_region_selected=None, auth= None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.auth = auth
        self.ui.setupUi(self)
        self.on_region_selected = on_region_selected

        self.ui.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.ui.scrollArea.horizontalScrollBar().setStyleSheet("height: 0px;")
        self.ui.scrollAreaWidgetContents.setMinimumWidth(5610)
        self.ui.scrollArea.setWidgetResizable(True)

        self.resize(960, 540)

        # Thiết lập background
        self.bg_label = QtWidgets.QLabel(self.ui.centralwidget)
        self.bg_label.setGeometry(0, 0, 960, 540)
        self.bg_label.setScaledContents(True)
        bg_path = os.path.abspath("images/mainwindow/bg.jpg")
        self.bg_pixmap = QtGui.QPixmap(bg_path)
        self.bg_label.setPixmap(self.bg_pixmap)

        self.opacity_effect = QtWidgets.QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.35)
        self.bg_label.setGraphicsEffect(self.opacity_effect)

        self.overlay = QtWidgets.QLabel(self.ui.centralwidget)
        self.overlay.setGeometry(0, 0, 960, 540)
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 300);")

        self.bg_label.lower()
        self.overlay.lower()

        self.set_styles()
        self.set_images()
        self.connect_buttons()
        self.ui.scrollArea.viewport().installEventFilter(self)

    def connect_buttons(self):
        self.ui.pushButtontbb.clicked.connect(self.open_tbb_window)
        self.ui.pushButtondbb.clicked.connect(self.open_dbb_window)

        self.ui.pushButtonbag.clicked.connect(self.open_bag)
        self.ui.pushButtonsetting.clicked.connect(self.open_settings)

    def open_tbb_window(self):
        self.tbb_window = TBBMainWindowExt(on_start_questions=self.show_again)
        self.tbb_window.show()
        self.close()

    def open_dbb_window(self):
        self.dbb_window = DBBMainWindowExt(on_start_questions=self.show_again)
        self.dbb_window.show()
        self.close()

    def show_again(self, region_name):
        print(f"Quay lại sau khi hoàn thành: {region_name}")
        self.show()

    def set_images(self):
        def set_icon(widget, path):
            icon_path = os.path.abspath(path)
            if os.path.exists(icon_path):
                widget.setIcon(QtGui.QIcon(icon_path))
            else:
                print(f"[⚠] Không tìm thấy ảnh: {icon_path}")

        set_icon(self.ui.pushButtontbb, "images/mainwindow/Tây Bắc Bộ.png")
        set_icon(self.ui.pushButtondbb, "images/mainwindow/Đông Bắc Bộ.png")
        set_icon(self.ui.pushButtondbsh, "images/mainwindow/Đồng bằng sông Hồng.png")
        set_icon(self.ui.pushButtonbtb, "images/mainwindow/Bắc Trung Bộ.png")
        set_icon(self.ui.pushButtonntb, "images/mainwindow/Nam Trung Bộ.png")
        set_icon(self.ui.pushButtontn, "images/mainwindow/Tây Nguyên.png")
        set_icon(self.ui.pushButtondbscl, "images/mainwindow/Đồng bằng sông Cửu Long.png")
        set_icon(self.ui.pushButtonbag, "images/mainwindow/bag.jpg")
        set_icon(self.ui.pushButtonsetting, "images/mainwindow/settings.jpg")

    def eventFilter(self, obj, event):
        if obj == self.ui.scrollArea.viewport():
            if event.type() == QtCore.QEvent.Type.Wheel:
                scroll_bar = self.ui.scrollArea.horizontalScrollBar()
                if scroll_bar.isVisible():
                    delta = event.angleDelta().y() or event.angleDelta().x()
                    scroll_bar.setValue(scroll_bar.value() - delta)
                    return True
            elif event.type() == QtCore.QEvent.Type.KeyPress:
                scroll_bar = self.ui.scrollArea.horizontalScrollBar()
                if scroll_bar.isVisible():
                    if event.key() == QtCore.Qt.Key.Key_Left:
                        scroll_bar.setValue(scroll_bar.value() - 50)
                        return True
                    elif event.key() == QtCore.Qt.Key.Key_Right:
                        scroll_bar.setValue(scroll_bar.value() + 50)
                        return True
        return super().eventFilter(obj, event)

    def set_styles(self):
        button_red_style = """
            QPushButton {
                background-color: rgb(162, 23, 23);
                border-radius: 5px;
                transition: background-color 0.3s ease;
            }
            QPushButton:hover {
                background-color: rgb(220, 50, 50);
            }
        """

        button_transparent_style = """
            QPushButton {
                background-color: transparent;
                border: none;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 80);
            }
        """

        label_style = """
            QLabel {
                font-size: 18pt;
                font-weight: bold;
                color: white;
                text-align: center;
            }
        """

        self.ui.pushButtonbag.setStyleSheet(button_red_style)
        self.ui.pushButtonsetting.setStyleSheet(button_red_style)

        transparent_buttons = [
            self.ui.pushButtontbb, self.ui.pushButtondbb, self.ui.pushButtondbsh,
            self.ui.pushButtonbtb, self.ui.pushButtonntb, self.ui.pushButtontn,
            self.ui.pushButtondbscl
        ]
        for btn in transparent_buttons:
            btn.setStyleSheet(button_transparent_style)

        labels = [
            self.ui.labeltbb, self.ui.labeldbb, self.ui.labeldbsh,
            self.ui.labeldbsh_2, self.ui.labelbtb, self.ui.labelntb,
            self.ui.labeltn, self.ui.labeldnb, self.ui.labeldbscl,
            self.ui.labeldbscl_2
        ]
        for lbl in labels:
            lbl.setStyleSheet(label_style)

    def show_region_info(self, region_name):
        if self.on_region_selected:
            self.on_region_selected(region_name)
        self.close()
        QtWidgets.QMessageBox.information(self, "Thông tin", f"Bạn đã chọn khu vực: {region_name}")

    def open_bag(self):
        QtWidgets.QMessageBox.information(self, "Túi đồ", "Tính năng túi đồ đang được phát triển.")

    def open_settings(self):
        QtWidgets.QMessageBox.information(self, "Cài đặt", "Tính năng cài đặt đang được phát triển.")
