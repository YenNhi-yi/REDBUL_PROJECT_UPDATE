import os
import json

from PyQt6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem

from Project.Controllers.AdminController import AdminController
from Project.ui.Admin_MainWindow import Ui_MainWindow


class Admin_MainWindowExt(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.controller = AdminController()

        self.pushButton_Input.clicked.connect(self.handle_input_question)
        self.pushButton_Delete.clicked.connect(self.handle_delete_question)
        self.pushButton_Update.clicked.connect(self.handle_update_question)
        self.pushButton_CreateTest.clicked.connect(self.handle_create_test)
        self.pushButton_InputCard.clicked.connect(self.select_image)

        self.comboBox_Province.currentTextChanged.connect(self.load_question_table)
        self.comboBox_Level.currentTextChanged.connect(self.load_question_table)
        self.load_question_table()

    def get_province_code(self, province):
        words = province.split()
        return ''.join([w[0] for w in words]).upper()

    def generate_question_id(self, province):
        filepath = os.path.join("data", "qsbanks.json")
        if not os.path.exists(filepath):
            return f"{province[:2].upper()}01"

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        count = 0
        if province in data:
            if isinstance(data[province], list):
                count = len(data[province])
            else:
                count = len(data[province].get("Easy", [])) + len(data[province].get("Hard", []))

        prefix = self.get_province_code(province)
        return f"{prefix}{count + 1:02d}"

    def handle_input_question(self):
        province = self.comboBox_Province.currentText()
        level = self.comboBox_Level.currentText()

        question = self.lineEditQuestion.text().strip()
        option_a = self.lineEditOptionA.text().strip()
        option_b = self.lineEditOptionB.text().strip()
        option_c = self.lineEditOptionC.text().strip()
        option_d = self.lineEditOptionD.text().strip()
        answer = self.lineEditAnswer.text().strip().upper()
        image_path = self.lineEditAnswer_Link.text().strip()

        if not all([question, option_a, option_b, option_c, option_d, answer]):
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng nhập đầy đủ câu hỏi và các lựa chọn.")
            return

        question_id = self.generate_question_id(province)

        question_data = {
            "id": question_id,
            "question": question,
            "options": {
                "A": option_a,
                "B": option_b,
                "C": option_c,
                "D": option_d
            },
            "answer": answer,
            "level": level,
            "culture_card": {
                "province": province,
                "image_path": image_path
            }
        }

        success = self.controller.add_question(province, level, question_data)

        if success:
            QMessageBox.information(self, "Thành công", f"Đã thêm câu hỏi cho tỉnh {province}.")
            self.clear_inputs()
            self.load_question_table()
        else:
            QMessageBox.critical(self, "Lỗi", "Không thể thêm câu hỏi.")

    def clear_inputs(self):
        self.lineEditQuestion.clear()
        self.lineEditOptionA.clear()
        self.lineEditOptionB.clear()
        self.lineEditOptionC.clear()
        self.lineEditOptionD.clear()
        self.lineEditAnswer.clear()
        self.lineEditAnswer_Link.clear()

    def handle_delete_question(self):
        row = self.tableWidgetList.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Chọn câu hỏi", "Vui lòng chọn câu hỏi cần xoá trong bảng.")
            return

        province = self.tableWidgetList.item(row, 0).text()
        level = self.tableWidgetList.item(row, 9).text()
        question_text = self.tableWidgetList.item(row, 2).text()

        confirm = QMessageBox.question(self, "Xác nhận xoá", f"Bạn chắc chắn muốn xoá câu hỏi:\n{question_text}?",
                                       QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirm == QMessageBox.StandardButton.Yes:
            if self.controller.delete_question(province, level, question_text):
                QMessageBox.information(self, "Đã xoá", "Câu hỏi đã được xoá.")
                self.load_question_table()
            else:
                QMessageBox.critical(self, "Lỗi", "Không thể xoá câu hỏi.")

    def handle_update_question(self):
        row = self.tableWidgetList.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Chọn câu hỏi", "Vui lòng chọn câu hỏi cần cập nhật trong bảng.")
            return

        old_question = self.tableWidgetList.item(row, 2).text()
        province = self.comboBox_Province.currentText()
        level = self.comboBox_Level.currentText()

        question = self.lineEditQuestion.text().strip()
        option_a = self.lineEditOptionA.text().strip()
        option_b = self.lineEditOptionB.text().strip()
        option_c = self.lineEditOptionC.text().strip()
        option_d = self.lineEditOptionD.text().strip()
        answer = self.lineEditAnswer.text().strip().upper()
        image_path = self.lineEditAnswer_Link.text().strip()

        if not all([question, option_a, option_b, option_c, option_d, answer]):
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng nhập đầy đủ các trường để cập nhật.")
            return

        question_id = self.tableWidgetList.item(row, 1).text()  # giữ nguyên ID

        new_data = {
            "id": question_id,
            "question": question,
            "options": {
                "A": option_a,
                "B": option_b,
                "C": option_c,
                "D": option_d
            },
            "answer": answer,
            "level": level,
            "culture_card": {
                "province": province,
                "image_path": image_path
            }
        }

        deleted = self.controller.delete_question(province, level, old_question)
        added = self.controller.add_question(province, level, new_data)

        if deleted and added:
            QMessageBox.information(self, "Thành công", "Cập nhật câu hỏi thành công!")
            self.clear_inputs()
            self.load_question_table()
        else:
            QMessageBox.critical(self, "Lỗi", "Không thể cập nhật câu hỏi.")

    def load_question_table(self):
        province = self.comboBox_Province.currentText()
        level = self.comboBox_Level.currentText()
        self.tableWidgetList.setRowCount(0)
        self.tableWidgetList.setColumnCount(10)
        self.tableWidgetList.setHorizontalHeaderLabels([
            "Province", "ID", "Question", "A", "B", "C", "D", "Answer", "Image", "Level"
        ])

        data = self.controller.get_questions_by_province_and_level(province, level)
        for i, q in enumerate(data):
            self.tableWidgetList.insertRow(i)
            self.tableWidgetList.setItem(i, 0, QTableWidgetItem(province))
            self.tableWidgetList.setItem(i, 1, QTableWidgetItem(q.get('id', '')))
            self.tableWidgetList.setItem(i, 2, QTableWidgetItem(q.get('question', '')))
            self.tableWidgetList.setItem(i, 3, QTableWidgetItem(q.get('options', {}).get('A', '')))
            self.tableWidgetList.setItem(i, 4, QTableWidgetItem(q.get('options', {}).get('B', '')))
            self.tableWidgetList.setItem(i, 5, QTableWidgetItem(q.get('options', {}).get('C', '')))
            self.tableWidgetList.setItem(i, 6, QTableWidgetItem(q.get('options', {}).get('D', '')))
            self.tableWidgetList.setItem(i, 7, QTableWidgetItem(q.get('answer', '')))
            self.tableWidgetList.setItem(i, 8, QTableWidgetItem(q.get('culture_card', {}).get('image_path', '')))
            self.tableWidgetList.setItem(i, 9, QTableWidgetItem(q.get('level', '')))

    def handle_create_test(self):
        filepath = os.path.join("data", "qsbanks.json")
        if not os.path.exists(filepath):
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy file câu hỏi qsbanks.json")
            return

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)

            easy_questions = []
            hard_questions = []

            for province_data in data.values():
                if isinstance(province_data, list):
                    easy_questions.extend(province_data)
                else:
                    easy_questions.extend(province_data.get("Easy", []))
                    hard_questions.extend(province_data.get("Hard", []))

            with open(os.path.join("data", "test_easy.json"), "w", encoding="utf-8") as f:
                json.dump(easy_questions, f, indent=4, ensure_ascii=False)

            with open(os.path.join("data", "test_hard.json"), "w", encoding="utf-8") as f:
                json.dump(hard_questions, f, indent=4, ensure_ascii=False)

            QMessageBox.information(self, "Thành công", "Đã tạo file test_easy.json và test_hard.json!")

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể tạo file test: {e}")

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Chọn ảnh thẻ văn hóa", "images/cards",
                                                   "Images (*.png *.jpg *.jpeg)")
        if file_path:
            relative_path = os.path.relpath(file_path, start=os.getcwd())
            self.lineEditAnswer_Link.setText(relative_path)