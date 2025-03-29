import json
import os

# Đảm bảo thư mục data tồn tại
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(data_dir, exist_ok=True)
# File regions.json xác định tỉnh nào thuộc miền nào
regions = {
    "TayBacBo": [
        "DienBien",
        "LaiChau",
        "SonLa",
        "HoaBinh",
        "YenBai",
        "LaoCai"
    ],
    "DongBacBo": [
        "CaoBang",
        "LangSon",
        "ThaiNguyen",
        "PhuTho",
        "TuyenQuang",
        "QuangNinh",
        "BacGiang"
    ],
    "DongBangSongHong": [
        "HaNoi",
        "HaiPhong",
        "NamDinh",
        "NinhBinh",
        "HaNam",
        "HungYen",
        "ThaiBinh",
        "VinhPhuc",
        "BacNinh"
    ],
    "BacTrungBo": [
        "ThanhHoa",
        "NgheAn",
        "HaTinh",
        "QuangBinh",
        "QuangTri",
        "ThuaThienHue"
    ],
    "DuyenHaiNamTrungBo": [
        "DaNang",
        "QuangNam",
        "QuangNgai",
        "BinhDinh",
        "PhuYen",
        "KhanhHoa",
        "NinhThuan",
        "BinhThuan"
    ],
    "TayNguyen": [
        "KonTum",
        "GiaLai",
        "DakLak",
        "DakNong",
        "LamDong"
    ],
    "DongNamBo": [
        "HoChiMinh",
        "BinhPhuoc",
        "BinhDuong",
        "DongNai",
        "TayNinh",
        "BaRiaVungTau"
    ],
    "DongBangSongCuuLong": [
        "LongAn",
        "TienGiang",
        "BenTre",
        "TraVinh",
        "VinhLong",
        "CanTho",
        "HauGiang",
        "SocTrang",
        "AnGiang",
        "KienGiang",
        "BacLieu",
        "CaMau"
    ]
}

# Ghi file regions.json
filepath = os.path.join(data_dir, "regions.json")
with open(filepath, "w", encoding="utf-8") as f:
    json.dump(regions, f, indent=4, ensure_ascii=False)

print(f"Đã tạo file {filepath}")
