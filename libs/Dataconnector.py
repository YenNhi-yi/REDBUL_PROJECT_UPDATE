import random

from Project.Models.Player import Player
from Project.libs.JisonFileFactory import JsonFileFactory


class DataConnector:
    def __init__(self):
        self.jff = JsonFileFactory()
        self.qsbanks = self.jff.read_data("data/qsbanks.json", dict)
        self.players = self.jff.read_data("data/players.json", Player)  # Fix lỗi tên hàm và class
        self.regions = self.jff.read_data("data/regions.json", dict)

    def get_player_by_username(self, username):
        for player in self.players:
            if player.username == username:
                return player
        return None

    def save_players(self):
        self.jff.write_data(self.players, "data/players.json")

    def create_player(self, username, password):
        new_player = Player(username=username, password=password, collected_cards=[])
        self.players.append(new_player)
        return new_player

    def get_all_regions(self):
        return self.regions

    def get_provinces_by_region(self, region_name):
        return self.regions.get(region_name, [])

    def get_questions_by_region(self, region_name):
        if region_name not in self.regions:
            return {}

        province_names = self.regions[region_name]
        result = {}
        for province in province_names:
            if province in self.qsbanks:
                result[province] = self.qsbanks[province]
        return result

    def get_questions_by_province(self, province_name):
        return self.qsbanks.get(province_name, [])

    def get_random_question_from_province(self, province):
        if province in self.qsbanks and self.qsbanks[province]:
            return random.choice(self.qsbanks[province])
        return None
