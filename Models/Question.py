from Project.Models.Culturecard import CultureCard


class Question:
    def __init__(self, id, content, options, answer, culture_card: CultureCard):
        self.id = id
        self.content = content
        self.options = options            # Dict: {"A": ..., "B": ...}
        self.answer = answer
        self.culture_card = culture_card  # CultureCard được nhận nếu trả lời đúng

    def is_correct(self, user_answer):
        return user_answer.upper() == self.answer.upper()

    def __str__(self):
        opts = "\n".join([f"{k}. {v}" for k, v in self.options.items()])
        return f"{self.content}\n{opts}\n(Đáp án đúng: {self.answer})"
