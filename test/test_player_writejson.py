import json
import os

# Đảm bảo thư mục data tồn tại
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(data_dir, exist_ok=True)

players = [
    {
        "username": "nhi",
        "password": "admin123",
        "role": "admin"
    },
    {
        "username": "teo",
        "password": "123",
        "role": "player",
        "unlocked_regions": ["TayBacBo"],
        "collected_cards": [
            {
                "province": "DienBien",
                "text": "Đồi A1 – Biểu tượng chiến thắng Điện Biên Phủ",
                "image_path": "images/cards/doi_a1.png"
            }
        ]
    },
    {
        "username": "ty",
        "password": "456",
        "role": "player",
        "unlocked_regions": ["TayBacBo", "DongBacBo"],
        "collected_cards": []
    }
]

filepath = os.path.join(data_dir, "players.json")
with open(filepath, "w", encoding="utf-8") as f:
    json.dump(players, f, indent=4, ensure_ascii=False)

print(f"Đã tạo file {filepath}")
