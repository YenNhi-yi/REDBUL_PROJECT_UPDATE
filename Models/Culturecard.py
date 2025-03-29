class CultureCard:
    def __init__(self, province, title, image):
        self.province = province      # Tỉnh/thành của thẻ
        self.title = title              # Mô tả ý nghĩa thẻ
        self.image = image  # Đường dẫn ảnh

    @classmethod
    def from_dict(cls,data):
        return CultureCard(
            province=data.get("province"),
            title=data.get("title"),  # map "text" → title
            image=data.get("image")  # map "image_path" → image
        )

    def to_dict(self):
        return {
            "province": self.province,
            "title": self.title,
            "image": self.image
        }

    def __str__(self):
        return f"[{self.province}] {self.title} - {self.image}"
