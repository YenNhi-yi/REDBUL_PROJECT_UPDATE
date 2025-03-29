import json
import os

filepath = os.path.join(os.path.dirname(__file__), '..', 'data', 'players.json')

with open(filepath, "r", encoding="utf-8") as f:
    player = json.load(f)

print(f"Người chơi: {player['username']}")
print("Danh sách thẻ văn hóa đã thu thập:")
for card in player["collected_cards"]:
    print(f"{card['province']}: {card['card']}")
