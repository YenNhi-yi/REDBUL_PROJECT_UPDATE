import json
import os
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QApplication

from Project.ui.Top10MainWindow import Ui_MainWindow


class Top10MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyle()
        self.load_leaderboard()
        self.ui.back.clicked.connect(self.close)

    def setStyle(self):
        self.ui.tabletop10.verticalHeader().setVisible(False)
        header = self.ui.tabletop10.horizontalHeader()
        for i in range(3):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

    def load_leaderboard(self):
        # Đường dẫn JSON cùng cấp với file chạy (an toàn nhất)
        json_path = os.path.join(os.path.dirname(__file__), "..", "data", "playersresult.json")

        with open(json_path, "r", encoding="utf-8") as f:
            players_data = json.load(f)

        top_players = sorted(players_data, key=lambda x: x["score"], reverse=True)[:10]
        emojis = ["🥇", "🥈", "🥉"]
        self.ui.tabletop10.setRowCount(10)

        for i, player in enumerate(top_players):
            rank = f"{emojis[i]} {i+1}" if i < 3 else str(i + 1)
            item_rank = QTableWidgetItem(rank)
            item_name = QTableWidgetItem(player["username"])
            item_score = QTableWidgetItem(str(player["score"]))

            for item in (item_rank, item_name, item_score):
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.ui.tabletop10.setItem(i, 0, item_rank)
            self.ui.tabletop10.setItem(i, 1, item_name)
            self.ui.tabletop10.setItem(i, 2, item_score)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Top10MainWindow()
    window.show()
    sys.exit(app.exec())
