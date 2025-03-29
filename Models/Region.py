class Region:
    def __init__(self, name, provinces):
        self.name = name                # Tên miền (Tây Bắc Bộ, Đông Bắc Bộ, ...)
        self.provinces = provinces      # List[Province]

    def is_completed(self):
        return all(p.answered for p in self.provinces)

    def __str__(self):
        return f"Miền {self.name} gồm {len(self.provinces)} tỉnh"
