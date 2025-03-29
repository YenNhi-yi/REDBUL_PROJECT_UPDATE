import json
import os

from Project.libs.Dataconnector import DataConnector


class AdminController:
    def __init__(self):
        self.dc = DataConnector()

    def get_all_players(self):
        return self.dc.players

    def get_all_regions(self):
        return list(self.dc.regions.keys())

    def get_all_provinces(self):
        provinces = set()
        for plist in self.dc.regions.values():
            provinces.update(plist)
        return sorted(list(provinces))

    def get_question_count_by_province(self, province):
        return len(self.dc.get_questions_by_province(province))

    def get_total_collected_cards(self, player):
        return len(player.collected_cards)

    def reset_player_progress(self, player):
        player.unlocked_regions = ["TayBacBo"]
        player.collected_cards = []
        self.dc.save_players()

    def add_question(self, province, level, question_data):
        try:
            filepath = os.path.join("data", "qsbanks.json")
            if os.path.exists(filepath):
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
            else:
                data = {}

            # Nếu tỉnh chưa tồn tại thì tạo mới
            if province not in data:
                data[province] = {"Easy": [], "Hard": []}
            elif isinstance(data[province], list):
                # Nếu đang ở định dạng cũ
                data[province] = {"Easy": data[province], "Hard": []}

            data[province][level].append(question_data)

            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            return True
        except Exception as e:
            print(f"[Error] add_question: {e}")
            return False

    def get_questions_by_province_and_level(self, province, level):
        filepath = os.path.join("data", "qsbanks.json")
        if not os.path.exists(filepath):
            return []

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        if province in data:
            if isinstance(data[province], list):
                return data[province]
            return data[province].get(level, [])
        return []

    def delete_question(self, province, level, question_text):
        try:
            filepath = os.path.join("data", "qsbanks.json")
            if not os.path.exists(filepath):
                return False

            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)

            if province not in data:
                return False

            if isinstance(data[province], list):
                data[province] = {"Easy": data[province], "Hard": []}

            questions = data[province].get(level, [])
            new_questions = [q for q in questions if q['question'] != question_text]

            if len(questions) == len(new_questions):
                return False

            data[province][level] = new_questions

            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            return True
        except Exception as e:
            print(f"[ERROR] delete_question: {e}")
            return False
