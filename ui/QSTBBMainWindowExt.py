import json
import os
import random
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow
from Project.Models.Culturecard import CultureCard
from Project.ui.CoLenExt import CoLenExt
from Project.ui.CorrectExt import CorrectExt
from Project.ui.QSTBBMainWindow import Ui_MainWindow

class QSTBBMainWindowExt(QMainWindow, Ui_MainWindow):
    def __init__(self, province_name, auth, level, current_player, on_question_complete=None):
        super().__init__()
        self.province_name = province_name
        self.level = level
        self.current_player = current_player
        self.auth = auth
        self.on_question_complete = on_question_complete

        self.setupUi(self)
        self.setup_events()
        self.setup_game_data()

        image_path = os.path.join("images", "qstbb.png")
        if os.path.exists(image_path):
            self.label.setPixmap(QPixmap(image_path))
            self.label.setScaledContents(True)
        else:
            print("Ảnh nền không tồn tại:", image_path)

        self.current_question = None
        self.previous_question = None
        self.provinces_answered = set()

        self.load_questions()

    def setup_game_data(self):
        filepath = os.path.join("data", "qsbanks.json")
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)

            province_data = data.get(self.province_name, {})
            self.questions = province_data.get(self.level, [])

            if not self.questions:
                print(f"Không có câu hỏi cho {self.province_name} - {self.level}")
            else:
                print(f"Tải {len(self.questions)} câu hỏi cho {self.province_name} - {self.level}")
        except Exception as e:
            print(f"[Error] setup_game_data: {e}")
            self.questions = []

    def setup_events(self):
        self.pushButton_A.clicked.connect(lambda: self.check_answer("A"))
        self.pushButton_B.clicked.connect(lambda: self.check_answer("B"))
        self.pushButton_C.clicked.connect(lambda: self.check_answer("C"))
        self.pushButton_D.clicked.connect(lambda: self.check_answer("D"))

    def load_questions(self):
        try:
            with open("data/test_easy.json", "r", encoding="utf-8") as file:
                all_questions = json.load(file)
                self.questions = [
                    q for q in all_questions
                    if q.get("culture_card", {}).get("province") == self.province_name
                ]
        except Exception as e:
            print(f"[⚠] Lỗi khi load câu hỏi: {e}")

    def check_answer(self, user_choice):
        correct_answer = self.current_question["answer"]
        if user_choice == correct_answer:
            card_info = self.current_question.get("culture_card", {})
            card = CultureCard(
                province=card_info.get("province", self.province_name),
                title=self.current_question["question"],
                image=card_info.get("image_path", "")
            )

            if self.current_player:
                self.current_player.add_card(card)
                self.auth.save_players()

            self.provinces_answered.add(self.province_name)
            if self.current_question in self.questions:
                self.questions.remove(self.current_question)

            image_path = card.image or "images/default.png"
            if not os.path.exists(image_path):
                image_path = "images/default.png"

            self.correct_popup = CorrectExt(
                image_path=image_path,
                on_next_callback=self.handle_correct_done
            )
            self.correct_popup.show()
        else:
            self.incorrect_popup = CoLenExt(on_next_callback=self.load_questions())
            self.incorrect_popup.show()

    def display_random_question(self):
        if not self.questions:
            print(f"[⚠] Không có câu hỏi cho {self.province_name} - {self.level}")
            return

        question = random.choice(self.questions)
        self.label_Qs.setText(question["question"])
        self.label_A.setText(f"A. {question['options']['A']}")
        self.label_B.setText(f"B. {question['options']['B']}")
        self.label_C.setText(f"C. {question['options']['C']}")
        self.label_D.setText(f"D. {question['options']['D']}")
        # Lưu câu hỏi hiện tại nếu cần xử lý sau
        self.current_question = question

    def handle_correct_done(self):
        self.load_questions()
