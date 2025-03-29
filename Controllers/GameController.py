from Project.libs import utils
from Project.libs.Dataconnector import DataConnector


class GameController:
    def __init__(self, auth):
        self.auth = auth
        self.dc = auth.dc
        self.dc = DataConnector()
        self.current_player = None
        self.regions_order = list(self.dc.regions.keys())  # Giữ đúng thứ tự miền

    def login(self, username):
        player = self.dc.get_player_by_username(username)
        if player:
            self.current_player = player
            return True
        return False

    def get_unlocked_regions(self):
        return self.current_player.unlocked_regions

    def unlock_next_region(self, current_region):
        next_region = utils.get_next_region(current_region, self.regions_order)
        if next_region and next_region not in self.current_player.unlocked_regions:
            self.current_player.unlocked_regions.append(next_region)
            self.dc.save_players()

    def answer_question(self, province, selected_answer):
        question = self.dc.get_random_question_from_province(province)
        if not question:
            return False, None

        if question["answer"] == selected_answer:
            # Thêm thẻ văn hóa
            card = question["culture_card"]
            if card not in self.current_player.collected_cards:
                self.current_player.collected_cards.append(card)
                self.dc.save_players()
            return True, card  # Trả lời đúng
        return False, None     # Trả lời sai

    def update_region_progress(self, region_name, province_name):
        """
        Ghi nhận rằng người chơi đã trả lời đúng ít nhất 1 câu hỏi của 1 tỉnh trong miền.
        Nếu số tỉnh được hoàn thành == tổng số tỉnh trong miền => mở miền tiếp theo.
        """
        if not hasattr(self.current_player, "region_progress"):
            self.current_player.region_progress = {}

        if region_name not in self.current_player.region_progress:
            self.current_player.region_progress[region_name] = set()

        self.current_player.region_progress[region_name].add(province_name)

        total_provinces = len(self.dc.regions.get(region_name, []))
        completed = len(self.current_player.region_progress[region_name])

        if completed >= total_provinces:
            self.unlock_next_region(region_name)