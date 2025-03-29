from PyQt6.QtWidgets import QMainWindow, QMessageBox
from Project.ui.QSDBSHMainWindow import Ui_MainWindow
import random


class QSDBSHMainWindowExt(QMainWindow, Ui_MainWindow):
    def __init__(self, questions: list[dict], on_correct_answer: callable):
        super().__init__()
        self.setupUi(self)
        self.questions = questions
        self.on_correct_answer = on_correct_answer
        self.current_question = None
        self.setup_events()
        self.load_random_question()

    def setup_events(self):
        self.pushButton_A.clicked.connect(lambda: self.check_answer("A"))
        self.pushButton_B.clicked.connect(lambda: self.check_answer("B"))
        self.pushButton_C.clicked.connect(lambda: self.check_answer("C"))
        self.pushButton_D.clicked.connect(lambda: self.check_answer("D"))

    def load_random_question(self):
        if not self.questions:
            QMessageBox.information(self, "Thông báo", "Hết câu hỏi trong tỉnh này!")
            self.close()
            return
        self.current_question = random.choice(self.questions)
        self.questions.remove(self.current_question)

        self.label_Qs.setText(self.current_question["question"])
        self.label_A.setText(self.current_question["options"]["A"])
        self.label_B.setText(self.current_question["options"]["B"])
        self.label_C.setText(self.current_question["options"]["C"])
        self.label_D.setText(self.current_question["options"]["D"])

    def check_answer(self, user_answer: str):
        correct = self.current_question["answer"].upper() == user_answer.upper()
        if correct:
            QMessageBox.information(self, "Chính xác!", "Bạn đã trả lời đúng và nhận được thẻ văn hóa!")
            if self.on_correct_answer:
                self.on_correct_answer(self.current_question)
            self.close()  # Đóng màn câu hỏi sau khi đúng
        else:
            QMessageBox.warning(self, "Sai rồi!", "Hãy thử lại với câu hỏi khác!")
            self.load_random_question()  # Random lại câu khác
