import json
import os

class JsonFileFactory:
    def __init__(self):
        pass

    def read_data(self, file_path, object_type=None):
        """
        Đọc dữ liệu từ JSON file và trả về object_type nếu có.
        - Nếu object_type là None → trả về raw dict/list
        - Nếu object_type là dict → trả về dict
        - Nếu object_type có from_dict() → chuyển dict thành object
        """
        if not os.path.exists(file_path):
            print(f"[!] File không tồn tại: {file_path}")
            return []

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Nếu không cần chuyển object
        if object_type is None:
            return data

        # Trường hợp dữ liệu là dict (vd: qsbank, regions)
        if object_type == dict:
            return data

        # Trường hợp dữ liệu là list object (vd: players)
        if isinstance(data, list):
            return [object_type.from_dict(item) for item in data]

        # Trường hợp object đơn
        return object_type.from_dict(data)

    def write_data(self, data, file_path):
        def convert(obj):
            if hasattr(obj, "to_dict"):
                return obj.to_dict()
            return obj  # dùng cho dict, string,...

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False, default=convert)

        print(f"[✓] Đã ghi dữ liệu vào: {file_path}")
