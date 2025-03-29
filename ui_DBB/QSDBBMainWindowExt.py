import os
import random

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QMessageBox

from Project.Controllers.AuthController import AuthController
from Project.Controllers.GameController import GameController
from Project.Controllers.RegionController import RegionController
from Project.Models.Culturecard import CultureCard
from Project.ui.CoLenExt import CoLenExt
from Project.ui.CorrectExt import CorrectExt
from Project.ui_DBB.DBB_HTExt import DBB_HTExt
from Project.ui_DBB.QSDBBMainWindow import Ui_MainWindow


class QSDBBMainWindowExt(QMainWindow, Ui_MainWindow):
    def __init__(self, province_name, on_question_complete=None, auth = None):
        super().__init__()
        self.setupUi(self)
        self.auth = auth

        image_path = os.path.join("images", "QSDBB.png")
        if os.path.exists(image_path):
            self.label.setPixmap(QPixmap(image_path))
            self.label.setScaledContents(True)
        else:
            print("Ảnh nền không tồn tại:", os.path.abspath(image_path))

        self.province_name = province_name
        self.on_question_complete = on_question_complete
        self.auth = AuthController()
        self.region_controller = RegionController(self.detect_region_from_province(province_name))

        self.questions = self.region_controller.dc.get_questions_by_province(province_name).copy()
        self.current_question = None
        self.previous_question = None
        self.provinces_answered = set()

        self.setup_events()
        self.load_question()

    def setup_events(self):
        self.pushButton_A.clicked.connect(lambda: self.check_answer("A"))
        self.pushButton_B.clicked.connect(lambda: self.check_answer("B"))
        self.pushButton_C.clicked.connect(lambda: self.check_answer("C"))
        self.pushButton_D.clicked.connect(lambda: self.check_answer("D"))

    def load_question(self):
        if not self.questions:
            print("[DEBUG] Không có câu hỏi để load.")
            self.ht_screen = DBB_HTExt(parent_to_close=self)
            self.ht_screen.show()
            return

        if len(self.questions) == 1:
            self.current_question = self.questions[0]
        else:
            while True:
                candidate = random.choice(self.questions)
                if candidate != self.previous_question:
                    self.current_question = candidate
                    break

        self.previous_question = self.current_question
        if "question" not in self.current_question or "options" not in self.current_question:
            QMessageBox.critical(self, "Lỗi dữ liệu", "Thiếu trường 'question' hoặc 'options'")
            self.close()
            return

        options = self.current_question["options"]

        self.label_Qs.setText(self.current_question["question"])
        self.label_A.setText(options.get("A", ""))
        self.label_B.setText(options.get("B", ""))
        self.label_C.setText(options.get("C", ""))
        self.label_D.setText(options.get("D", ""))

    def check_answer(self, user_choice):
        correct_answer = self.current_question["answer"]
        if user_choice == correct_answer:
            card_info = self.current_question.get("culture_card", {})
            card_info.setdefault("province", self.province_name)
            card_info.setdefault("title", self.current_question["question"])
            card_info.setdefault("image", card_info.get("image_path", "images/default.png"))
            card = CultureCard.from_dict(card_info)

            player = self.auth.get_current_player()
            if not player:
                QMessageBox.critical(self, "Lỗi người chơi", "Không tìm thấy người chơi hiện tại!")
                return

            player.add_card(card)
            self.auth.save_players()

            self.provinces_answered.add(self.province_name)
            if self.current_question in self.questions:
                self.questions.remove(self.current_question)

            image_path = card.image or "images/default.png"
            if not os.path.exists(image_path):
                print(f"[⚠] Không tìm thấy ảnh thẻ: {os.path.abspath(image_path)}")
                image_path = "images/default.png"

            self.correct_popup = CorrectExt(
                image_path=image_path,
                on_next_callback=self.handle_correct_done
            )
            self.correct_popup.show()
        else:
            self.incorrect_popup = CoLenExt(on_next_callback=self.load_question)
            self.incorrect_popup.show()

    def detect_region_from_province(self, province_name):
        from Project.libs.Dataconnector import DataConnector
        dc = DataConnector()
        for region, provinces in dc.regions.items():
            if province_name in provinces:
                return region
        return "DongBacBo"

    def handle_correct_done(self):
        game = GameController()
        game.login(self.auth.get_current_player().username)  # đảm bảo đang gán current_player

        game.update_region_progress(
            region_name=self.region_controller.region_name,
            province_name=self.province_name)
        self.load_question()
