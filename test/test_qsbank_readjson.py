import json
import os

filepath = os.path.join(os.path.dirname(__file__), '..', 'data', 'qsbanks.json')

with open(filepath, "r", encoding="utf-8") as f:
    qsbanks = json.load(f)

# In ra thông tin câu hỏi đầu tiên của Điện Biên
for question in qsbanks["DienBien"]:
    print(f"Câu hỏi: {question['question']}")
    print(f"Đáp án đúng: {question['answer']}")
    print(f"Thẻ văn hóa: {question['culture_card']}")
    print("---")
