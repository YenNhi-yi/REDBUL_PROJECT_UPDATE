from Project.Models.Culturecard import CultureCard


class Player:
    def __init__(self, username, password, collected_cards=None, unlocked_regions=None, region_progress=None):
        self.username = username
        self.password = password
        self.collected_cards = collected_cards or []
        self.unlocked_regions = unlocked_regions or ["TayBacBo"]
        self.region_progress = region_progress or {}
    def unlock_region(self, region_name):
        if region_name not in self.unlocked_regions:
            self.unlocked_regions.append(region_name)

    def has_card(self, province_name):
        return any(card.province == province_name for card in self.collected_cards)

    def add_card(self, card: CultureCard):
        if not self.has_card(card.province):
            self.collected_cards.append(card)

    def __str__(self):
        return f"{self.username} | Mở: {self.unlocked_regions} | Thẻ: {len(self.collected_cards)}"

    @classmethod
    def from_dict(cls, data):
        collected_cards = [CultureCard.from_dict(card) for card in data.get("collected_cards", [])]
        return cls(
            username=data.get("username", ""),
            password=data.get("password", ""),
            unlocked_regions=data.get("unlocked_regions", []),
            collected_cards=collected_cards
        )

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "unlocked_regions": self.unlocked_regions,
            "collected_cards": [card.to_dict() for card in self.collected_cards]
        }
