from random import random


class Province:
    def __init__(self, name, questions):
        self.name = name              # Tên tỉnh
        self.questions = questions    # List[Question]
        self.answered = False         # Đã trả lời đúng tỉnh này chưa?

    def get_random_question(self):
        return random.choice(self.questions)

    def __str__(self):
        return f"Tỉnh {self.name} ({len(self.questions)} câu hỏi)"
