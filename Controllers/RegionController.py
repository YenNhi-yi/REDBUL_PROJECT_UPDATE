import random

from Project.libs.Dataconnector import DataConnector


class RegionController:
    def __init__(self, region_name):
        self.dc = DataConnector()
        self.region_name = region_name
        self.provinces = self.dc.regions.get(region_name, [])
        self.remaining_provinces = self.provinces.copy()
        random.shuffle(self.remaining_provinces)
        self.current_province = None

    def get_province_names(self):
        return self.provinces

    def get_questions_for_province(self, province_name):
        return self.dc.get_questions_by_province(province_name)

    def get_next_province(self):
        if self.remaining_provinces:
            self.current_province = self.remaining_provinces.pop(0)
            return self.current_province
        return None

    def get_question(self):
        if self.current_province:
            return self.dc.get_random_question_from_province(self.current_province)
        return None

    def is_region_completed(self):
        return len(self.remaining_provinces) == 0

    def get_current_province(self):
            return self.current_province