import json
import os

# Đảm bảo thư mục data tồn tại
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(data_dir, exist_ok=True)

# Dữ liệu câu hỏi hoàn chỉnh cho 6 tỉnh Tây Bắc Bộ (bao gồm culture_card cho từng câu)
raw_qsbanks = {
    "DienBien": [
        {
            "question": "Đâu là tên di tích lịch sử tại Điện Biên?",
            "options": {
                "A": "Thành Nhà Hồ",
                "B": "Đồi A1",
                "C": "Cố đô Hoa Lư",
                "D": "Chùa Một Cột"
            },
            "answer": "B",
            "culture_card": {
                "province": "DienBien",
                "image_path": "images/cards/doi_a1.png"
            }
        },
        {
            "question": "Món ăn nào sau đây là đặc sản Điện Biên?",
            "options": {
                "A": "Chả rươi",
                "B": "Thắng cố",
                "C": "Pa pỉnh tộp",
                "D": "Bánh cuốn chả"
            },
            "answer": "C",
            "culture_card": {
                "province": "DienBien",
                "image_path": "images/cards/pa_pinh_top.png"
            }
        },
        {
          "question": "Bức ảnh dưới đây chụp di tích nào của Điện Biên?",
            "options": {
                "A": "Đồi A1",
                "B": "Hầm Đờ Cát",
                "C": "Cột mốc biên giới",
                "D": "Bảo tàng Chiến thắng Điện Biên Phủ"
            },
            "answer": "B",
            "culture_card": {
                "province": "DienBien",
                "image_path": "images/cards/ham_do_cat.png"
            }
        },
        {
            "question": "Điện Biên là nơi diễn ra trận chiến lịch sử năm ____ giữa quân đội Việt Nam và Pháp.",
            "options": {
                "A": "1945",
                "B": "1950",
                "C": "1954",
                "D": "1975"
            },
            "answer": "C",
            "culture_card": {
                "province": "DienBien",
                "image_path": "images/cards/dien_bien_phu.png"
            }
        }
    ],
    "HoaBinh": [
        {
            "question": "Con sông nào chảy qua tỉnh Hòa Bình?",
            "options": {
                "A": "Sông Hồng",
                "B": "Sông Mã",
                "C": "Sông Đà",
                "D": "Sông Lô"
            },
            "answer": "C",
            "culture_card": {
                "province": "HoaBinh",
                "image_path": "images/cards/song_da.png"
            }
        },
        {
            "question": "Danh thắng nào sau đây thuộc Hòa Bình?",
            "options": {
                "A": "Động Phong Nha",
                "B": "Hồ Ba Bể",
                "C": "Thung Nai",
                "D": "Động Thiên Đường"
            },
            "answer": "C",
            "culture_card": {
                "province": "HoaBinh",
                "image_path": "images/cards/thung_nai.png"
            }
        },
        {
            "question": "Để làm món “Chả cuốn lá bưởi”, người ta không dùng nguyên liệu nào sau đây?",
            "options": {
                "A": "Thịt lợn băm",
                "B": "Lá bưởi",
                "C": "Gạo nếp",
                "D": "Mắc khén"
            },
            "answer": "C",
            "culture_card": {
                "province": "HoaBinh",
                "image_path": "images/cards/cha_cuon_la_buoi.png"
            }
        },
        {
            "question": "Dân tộc Mường ở Hòa Bình có lễ hội đặc trưng là lễ hội _____.",
            "options": {
                "A": "Gầu Tào",
                "B": "Cầu Mùa",
                "C": "Chọi trâu",
                "D": "Kate"
            },
            "answer": "B",
            "culture_card": {
                "province": "HoaBinh",
                "image_path": "images/cards/cau_mua.png"
            }
        }
    ],
    "LaiChau": [
        {
            "question": "Đỉnh núi cao nhất ở Lai Châu là gì?",
            "options": {
                "A": "Fansipan",
                "B": "Pu Ta Leng",
                "C": "Tây Côn Lĩnh",
                "D": "Bạch Mộc Lương Tử"
            },
            "answer": "B",
            "culture_card": {
                "province": "LaiChau",
                "image_path": "images/cards/pu_ta_leng.png"
            }
        },
        {
            "question": "Đặc sản nào nổi tiếng của Lai Châu?",
            "options": {
                "A": "Thắng cố",
                "B": "Mận tam hoa",
                "C": "Nem nướng",
                "D": "Bánh pía"
            },
            "answer": "B",
            "culture_card": {
                "province": "LaiChau",
                "image_path": "images/cards/man_tam_hoa.png"
            }
        },
        {
            "question": "Nguyên liệu nào sau đây không cần thiết cho món lợn cắp nách nướng?",
            "options": {
                "A": "Thịt lợn cắp nách",
                "B": "Hạt dổi",
                "C": "Rau má",
                "D": "Mắc khén"
            },
            "answer": "C",
            "culture_card": {
                "province": "LaiChau",
                "image_path": "images/cards/lon_cap_nach.png"
            }
        },
        {
            "question": "Đèo Ô Quy Hồ còn có tên gọi khác là đèo _____.",
            "options": {
                "A": "Hải Vân",
                "B": "Hoàng Liên Sơn",
                "C": "Pha Đin",
                "D": "Mã Pí Lèng"
            },
            "answer": "B",
            "culture_card": {
                "province": "LaiChau",
                "image_path": "images/cards/o_quy_ho.png"
            }
        }
    ],
    "SonLa": [
        {
            "question": "Đặc sản nào nổi tiếng nhất của Sơn La?",
            "options": {
                "A": "Cơm lam",
                "B": "Chẳm chéo",
                "C": "Cá kho tộ",
                "D": "Nem chua"
            },
            "answer": "B",
            "culture_card": {
                "province": "SonLa",
                "image_path": "images/cards/cham_cheo.png"
            }
        },
        {
            "question": "Lễ hội Hoa Ban là lễ hội của dân tộc nào ở Sơn La?",
            "options": {
                "A": "Thái",
                "B": "Mông",
                "C": "Dao",
                "D": "Tày"
            },
            "answer": "A",
            "culture_card": {
                "province": "SonLa",
                "image_path": "images/cards/hoa_ban.png"
            }
        },
        {
            "question": "Nguyên liệu chính để làm sữa Mộc Châu là gì?",
            "options": {
                "A": "Sữa bò tươi",
                "B": "Gạo nếp",
                "C": "Khoai lang",
                "D": "Đậu xanh"
            },
            "answer": "A",
            "culture_card": {
                "province": "SonLa",
                "image_path": "images/cards/sua_moc_chau.png"
            }
        },
        {
            "question": "Nhà máy thủy điện lớn nhất Việt Nam nằm ở tỉnh nào?",
            "options": {
                "A": "Lai Châu",
                "B": "Sơn La",
                "C": "Hòa Bình",
                "D": "Ialy"
            },
            "answer": "B",
            "culture_card": {
                "province": "SonLa",
                "image_path": "images/cards/thuy_dien_sonla.png"
            }
        }
    ],
    "LaoCai": [
        {
            "question": "Địa danh nổi tiếng nhất của Lào Cai là gì?",
            "options": {
                "A": "Tây Côn Lĩnh",
                "B": "Fansipan",
                "C": "Bạch Mộc Lương Tử",
                "D": "Phan Si Păng"
            },
            "answer": "B",
            "culture_card": {
                "province": "LaoCai",
                "image_path": "images/cards/fansipan.png"
            }
        },
        {
            "question": "Sông lớn nào chảy qua thành phố Lào Cai?",
            "options": {
                "A": "Sông Hồng",
                "B": "Sông Đà",
                "C": "Sông Lô",
                "D": "Sông Chảy"
            },
            "answer": "A",
            "culture_card": {
                "province": "LaoCai",
                "image_path": "images/cards/song_hong.png"
            }
        },
        {
            "question": "Lào Cai nổi tiếng với loại hình nghệ thuật nào?",
            "options": {
                "A": "Hát Then",
                "B": "Hát Xoan",
                "C": "Hát Páo Dung",
                "D": "Hát Quan Họ"
            },
            "answer": "C",
            "culture_card": {
                "province": "LaoCai",
                "image_path": "images/cards/pao_dung.png"
            }
        },
        {
            "question": "Món ăn nào thường xuất hiện trong phiên chợ vùng cao ở Lào Cai?",
            "options": {
                "A": "Phở chua",
                "B": "Cháo ấu tẩu",
                "C": "Bánh đúc nóng",
                "D": "Thắng cố"
            },
            "answer": "D",
            "culture_card": {
                "province": "LaoCai",
                "image_path": "images/cards/thang_co.png"
            }
        },
        {
            "question": "Nguyên liệu chính để làm rượu ngô Bắc Hà?",
            "options": {
                "A": "Gạo nếp nương",
                "B": "Ngô hạt địa phương",
                "C": "Khoai lang",
                "D": "Đậu xanh"
            },
            "answer": "B",
            "culture_card": {
                "province": "LaoCai",
                "image_path": "images/cards/ruou_ngo.png"
            }
        }
    ],
    "YenBai": [
        {
            "question": "Đặc sản nào sau đây là của Yên Bái?",
            "options": {
                "A": "Cơm lam Bắc Mê",
                "B": "Thịt trâu gác bếp",
                "C": "Chè Shan tuyết Suối Giàng",
                "D": "Cá thính Phú Thọ"
            },
            "answer": "C",
            "culture_card": {
                "province": "YenBai",
                "image_path": "images/cards/che_suoi_giang.png"
            }
        },
        {
            "question": "Danh thắng nào nổi tiếng nhất ở Yên Bái?",
            "options": {
                "A": "Ruộng bậc thang Mù Cang Chải",
                "B": "Hồ Ba Bể",
                "C": "Thác Bản Giốc",
                "D": "Cao nguyên đá Đồng Văn"
            },
            "answer": "A",
            "culture_card": {
                "province": "YenBai",
                "image_path": "images/cards/mu_cang_chai.png"
            }
        },
        {
            "question": "Nguyên liệu nào không dùng để làm 'Muồm muỗm rang'?",
            "options": {
                "A": "Muồm muỗm",
                "B": "Hạt mắc khén",
                "C": "Lá lốt",
                "D": "Lá chanh"
            },
            "answer": "C",
            "culture_card": {
                "province": "YenBai",
                "image_path": "images/cards/muom_muom.png"
            }
        },
        {
            "question": "Đèo Khau Phạ thuộc huyện nào?",
            "options": {
                "A": "Mù Cang Chải",
                "B": "Văn Chấn",
                "C": "Trạm Tấu",
                "D": "Yên Bình"
            },
            "answer": "A",
            "culture_card": {
                "province": "YenBai",
                "image_path": "images/cards/khau_pha.png"
            }
        }
    ],
    "HaNoi": [
        {
            "question": "Lễ hội nào nổi tiếng ở Hà Nội được tổ chức để tưởng nhớ Thánh Gióng?",
            "options": {
                "A": "Lễ hội Đền Hùng",
                "B": "Lễ hội Tràng An",
                "C": "Lễ hội Gióng",
                "D": "Lễ hội Yên Thế"
            },
            "answer": "C",
            "culture_card": {
                "province": "HaNoi",
               "image_path": "images/cards/leloi_giong.png"
            }
        },
        {
            "question": "Ai là người dời đô từ Hoa Lư ra Thăng Long?",
            "options": {
                "A": "Lý Thái Tổ",
                "B": "Ngô Quyền",
                "C": "Trần Thái Tông",
                "D": "Lê Lợi"
            },
            "answer": "A",
            "culture_card": {
                "province": "HaNoi",
                "image_path": "images/cards/ly_thai_to.png"
            }
        },
        {
            "question": "Món ăn nào là đặc sản nổi tiếng gắn liền với Hà Nội?",
            "options": {
                "A": "Bún bò Huế",
                "B": "Phở Hà Nội",
                "C": "Mì Quảng",
                "D": "Bánh xèo"
            },
            "answer": "B",
            "culture_card": {
                "province": "HaNoi",
                "image_path": "images/cards/pho_ha_noi.png"
            }
        },
        {
            "question": "Văn Miếu – Quốc Tử Giám được xây dựng vào thời nào?",
            "options": {
                "A": "Thời Lý",
                "B": "Thời Trần",
                "C": "Thời Lê",
                "D": "Thời Nguyễn"
            },
            "answer": "A",
            "culture_card": {
                "province": "HaNoi",
                "image_path": "images/cards/van_mieu.png"
            }
        }
    ],
    "HaiPhong": [
        {
            "question": "Hải Phòng nổi tiếng với lễ hội nào sau đây?",
            "options": {
                "A": "Lễ hội Đền Trần",
                "B": "Lễ hội Gióng",
                "C": "Lễ hội Chọi trâu Đồ Sơn",
                "D": "Lễ hội Lam Kinh"
            },
            "answer": "C",
            "culture_card": {
                "province": "HaiPhong",
                "image_path": "images/cards/choi_trau.png"
            }
        },
        {
            "question": "Món ăn nào là đặc sản nổi tiếng của Hải Phòng?",
            "options": {
                "A": "Bánh đúc nóng",
                "B": "Bánh đa cua",
                "C": "Bánh tẻ",
                "D": "Bún mắm"
            },
            "answer": "B",
            "culture_card": {
                "province": "HaiPhong",
                "image_path": "images/cards/banh_da_cua.png"
            }
        },
        {
            "question": "Bãi biển nổi tiếng ở Hải Phòng tên là gì?",
            "options": {
                "A": "Cửa Lò",
                "B": "Đồ Sơn",
                "C": "Trà Cổ",
                "D": "Bãi Cháy"
            },
            "answer": "B",
            "culture_card": {
                "province": "HaiPhong",
                "image_path": "images/cards/do_son.png"
            }
        },
        {
            "question": "Hải Phòng từng là căn cứ quan trọng trong cuộc kháng chiến chống thực dân nào?",
            "options": {
                "A": "Pháp",
                "B": "Mỹ",
                "C": "Mông",
                "D": "Minh"
            },
            "answer": "A",
            "culture_card": {
                "province": "HaiPhong",
                "image_path": "images/cards/khang_chien_phap.png"
            }
        }
    ],
    "HungYen": [
        {
            "question": "Trái cây nào là đặc sản nổi tiếng của Hưng Yên?",
            "options": {
                "A": "Cam Xã Đoài",
                "B": "Nhãn lồng",
                "C": "Vải thiều",
                "D": "Mít Tố Nữ"
            },
            "answer": "B",
            "culture_card": {
                "province": "HungYen",
                "image_path": "images/cards/nhan_long.png"
            }
        },
        {
            "question": "Thị xã nào xưa kia từng là trung tâm giao thương sầm uất của Hưng Yên?",
            "options": {
                "A": "Phố Hiến",
                "B": "Chợ Bến Thành",
                "C": "Phố cổ Hội An",
                "D": "Chợ Đồng Xuân"
            },
            "answer": "A",
            "culture_card": {
                "province": "HungYen",
                "image_path": "images/cards/pho_hien.png"
            }
        },
        {
            "question": "Hưng Yên có làng nghề truyền thống nổi tiếng nào?",
            "options": {
                "A": "Làng gốm Bát Tràng",
                "B": "Làng Nôm",
                "C": "Làng tranh Đông Hồ",
                "D": "Làng rối nước"
            },
            "answer": "B",
            "culture_card": {
                "province": "HungYen",
                "image_path": "images/cards/lang_nom.png"
            }
        },
        {
            "question": "Chợ nổi tiếng gắn liền với lịch sử Phố Hiến tên là gì?",
            "options": {
                "A": "Chợ Gạo",
                "B": "Chợ Phố Cũ",
                "C": "Chợ Ninh",
                "D": "Chợ Thượng"
            },
            "answer": "A",
            "culture_card": {
                "province": "HungYen",
                "image_path": "images/cards/cho_gao.png"
            }
        }
    ],
    "HaiDuong": [
        {
            "question": "Lễ hội nào nổi tiếng ở Côn Sơn – Kiếp Bạc, Hải Dương?",
            "options": {
                "A": "Lễ hội Đền Trần",
                "B": "Lễ hội Gióng",
                "C": "Lễ hội Kiếp Bạc",
                "D": "Lễ hội Chọi trâu"
            },
            "answer": "C",
            "culture_card": {
                "province": "HaiDuong",
                "image_path": "images/cards/kiep_bac.png"
            }
        },
        {
            "question": "Danh nhân Nguyễn Trãi từng sống và làm việc tại địa danh nào ở Hải Dương?",
            "options": {
                "A": "Côn Sơn",
                "B": "Tam Đảo",
                "C": "Yên Tử",
                "D": "Ba Vì"
            },
            "answer": "A",
            "culture_card": {
                "province": "HaiDuong",
                "image_path": "images/cards/con_son.png"
            }
        },
        {
            "question": "Di tích Côn Sơn – Kiếp Bạc gắn với nhân vật lịch sử nào?",
            "options": {
                "A": "Hưng Đạo Vương",
                "B": "Lê Lợi",
                "C": "Ngô Quyền",
                "D": "Triệu Thị Trinh"
            },
            "answer": "A",
            "culture_card": {
                "province": "HaiDuong",
                "image_path": "images/cards/con_son_kiep_bac.png"
            }
        }
    ],
    "BacNinh": [
        {
            "question": "Dân ca Quan họ là di sản văn hóa nổi tiếng của tỉnh nào?",
            "options": {
                "A": "Hà Nam",
                "B": "Bắc Ninh",
                "C": "Thái Nguyên",
                "D": "Vĩnh Phúc"
            },
            "answer": "B",
            "culture_card": {
                "province": "BacNinh",
                "image_path": "images/cards/quan_ho.png"
            }
        },
        {
            "question": "Kinh Bắc là tên gọi xưa của tỉnh nào ngày nay?",
            "options": {
                "A": "Hà Nội",
                "B": "Hưng Yên",
                "C": "Bắc Ninh",
                "D": "Hải Dương"
            },
            "answer": "C",
            "culture_card": {
                "province": "BacNinh",
                "image_path": "images/cards/kinh_bac.png"
            }
        },
        {
            "question": "Món bánh phu thê là đặc sản của tỉnh nào?",
            "options": {
                "A": "Nam Định",
                "B": "Hà Nội",
                "C": "Bắc Ninh",
                "D": "Hải Phòng"
            },
            "answer": "C",
            "culture_card": {
                "province": "BacNinh",
                "image_path": "images/cards/banh_phu_the.png"
            }
        },
        {
            "question": "Làng tranh Đông Hồ thuộc tỉnh nào?",
            "options": {
                "A": "Bắc Giang",
                "B": "Bắc Ninh",
                "C": "Thái Bình",
                "D": "Nam Định"
            },
            "answer": "B",
            "culture_card": {
                "province": "BacNinh",
                "image_path": "images/cards/tranh_dong_ho.png"
            }
        }
    ],
    "NamDinh": [
        {
            "question": "Lễ hội Phủ Dầy ở Nam Định thờ ai?",
            "options": {
                "A": "Bà Trưng",
                "B": "Chúa Liễu Hạnh",
                "C": "Thánh Mẫu Thoải",
                "D": "Bà Triệu"
            },
            "answer": "B",
            "culture_card": {
                "province": "NamDinh",
                "image_path": "images/cards/phu_day.png"
            }
        },
        {
            "question": "Nam Định là nơi khai sinh của triều đại phong kiến nào?",
            "options": {
                "A": "Nhà Trần",
                "B": "Nhà Lý",
                "C": "Nhà Lê",
                "D": "Nhà Nguyễn"
            },
            "answer": "A",
            "culture_card": {
                "province": "NamDinh",
                "image_path": "images/cards/nha_tran.png"
            }
        },
        {
            "question": "Đặc sản nổi tiếng nào của Nam Định thường dùng trong các dịp lễ tết?",
            "options": {
                "A": "Bánh cốm",
                "B": "Bánh gai",
                "C": "Kẹo Sìu Châu",
                "D": "Bánh ít"
            },
            "answer": "C",
            "culture_card": {
                "province": "NamDinh",
                "image_path": "images/cards/keo_siu_chau.png"
            }
        },
        {
            "question": "Nhà thờ lớn Phú Nhai ở Nam Định thuộc huyện nào?",
            "options": {
                "A": "Trực Ninh",
                "B": "Xuân Trường",
                "C": "Hải Hậu",
                "D": "Giao Thủy"
            },
            "answer": "B",
            "culture_card": {
                "province": "NamDinh",
                "image_path": "images/cards/nha_tho_phu_nhai.png"
            }
        }
    ],
    "NinhBinh": [
        {
            "question": "Khu di sản nào ở Ninh Bình được UNESCO công nhận là Di sản Văn hóa và Thiên nhiên thế giới?",
            "options": {
                "A": "Tam Cốc – Bích Động",
                "B": "Tràng An",
                "C": "Vườn quốc gia Cúc Phương",
                "D": "Chùa Bái Đính"
            },
            "answer": "B",
            "culture_card": {
                "province": "NinhBinh",
                "image_path": "images/cards/trang_an.png"
            }
        },
        {
            "question": "Kinh đô Hoa Lư – cố đô đầu tiên của nước Đại Cồ Việt – gắn với vị vua nào?",
            "options": {
                "A": "Lý Thái Tổ",
                "B": "Lê Đại Hành",
                "C": "Đinh Tiên Hoàng",
                "D": "Trần Nhân Tông"
            },
            "answer": "C",
            "culture_card": {
                "province": "NinhBinh",
                "image_path": "images/cards/hoa_lu.png"
            }
        },
        {
            "question": "Món ăn nào sau đây là đặc sản nổi tiếng của Ninh Bình?",
            "options": {
                "A": "Thịt trâu gác bếp",
                "B": "Cá kho làng Vũ Đại",
                "C": "Cơm cháy Ninh Bình",
                "D": "Bánh gai Tứ Trụ"
            },
            "answer": "C",
            "culture_card": {
                "province": "NinhBinh",
                "image_path": "images/cards/com_chay.png"
            }
        },
        {
            "question": "Chùa Bái Đính nổi tiếng vì điều gì?",
            "options": {
                "A": "Ngôi chùa cổ nhất Việt Nam",
                "B": "Chùa nằm trên đỉnh núi cao nhất",
                "C": "Quần thể chùa lớn nhất Đông Nam Á",
                "D": "Nơi có pho tượng Phật ngọc duy nhất"
            },
            "answer": "C",
            "culture_card": {
                "province": "NinhBinh",
                "image_path": "images/cards/bai_dinh.png"
            }
        }
    ],
    "ThaiBinh": [
        {
            "question": "Tỉnh Thái Bình nổi tiếng với điệu múa dân gian nào?",
            "options": {
                "A": "Múa rối cạn",
                "B": "Múa lân",
                "C": "Múa chèo",
                "D": "Múa rối nước"
            },
            "answer": "D",
            "culture_card": {
                "province": "ThaiBinh",
                "image_path": "images/cards/roi_nuoc.png"
            }
        },
        {
            "question": "Ngôi chùa nào nổi tiếng ở Thái Bình và được mệnh danh là 'Đệ nhất danh lam'? ",
            "options": {
                "A": "Chùa Keo",
                "B": "Chùa Dâu",
                "C": "Chùa Bái Đính",
                "D": "Chùa Thiên Mụ"
            },
            "answer": "A",
            "culture_card": {
                "province": "ThaiBinh",
                "image_path": "images/cards/chua_keo.png"
            }
        },
        {
            "question": "Món ăn nào sau đây là đặc sản của Thái Bình?",
            "options": {
                "A": "Bánh gai",
                "B": "Canh cá Quỳnh Côi",
                "C": "Bánh cuốn Thanh Trì",
                "D": "Bún riêu cua"
            },
            "answer": "B",
            "culture_card": {
                "province": "ThaiBinh",
                "image_path": "images/cards/canh_ca.png"
            }
        },
        {
            "question": "Tỉnh Thái Bình thuộc vùng địa lý nào của Việt Nam?",
            "options": {
                "A": "Tây Bắc Bộ",
                "B": "Đông Bắc Bộ",
                "C": "Đồng bằng sông Hồng",
                "D": "Duyên hải Nam Trung Bộ"
            },
            "answer": "C",
            "culture_card": {
                "province": "ThaiBinh",
                "image_path": "images/cards/thai_binh.png"
            }
        }
    ],
    "HaNam": [
        {
            "question": "Ngôi chùa Tam Chúc nổi tiếng của Hà Nam được mệnh danh là gì?",
            "options": {
                "A": "Chùa trên núi cao nhất",
                "B": "Ngôi chùa cổ nhất",
                "C": "Ngôi chùa lớn nhất thế giới",
                "D": "Ngôi chùa linh thiêng nhất miền Trung"
            },
            "answer": "C",
            "culture_card": {
                "province": "HaNam",
                "image_path": "images/cards/chua_tam_chuc.png"
            }
        },
        {
            "question": "Hà Nam nằm bên dòng sông lớn nào của miền Bắc Việt Nam?",
            "options": {
                "A": "Sông Hồng",
                "B": "Sông Đáy",
                "C": "Sông Cầu",
                "D": "Sông Mã"
            },
            "answer": "B",
            "culture_card": {
                "province": "HaNam",
                "image_path": "images/cards/song_day.png"
            }
        },
        {
            "question": "Đặc sản nổi tiếng nào sau đây có nguồn gốc từ Hà Nam?",
            "options": {
                "A": "Chuối ngự Đại Hoàng",
                "B": "Nem chua Thanh Hóa",
                "C": "Phở cuốn",
                "D": "Bánh tét"
            },
            "answer": "A",
            "culture_card": {
                "province": "HaNam",
                "image_path": "images/cards/chuoi_ngu.png"
            }
        },
        {
            "question": "Hà Nam thuộc vùng nào của Việt Nam?",
            "options": {
                "A": "Tây Bắc Bộ",
                "B": "Bắc Trung Bộ",
                "C": "Đồng bằng sông Hồng",
                "D": "Đông Nam Bộ"
            },
            "answer": "C",
            "culture_card": {
                "province": "HaNam",
                "image_path": "images/cards/ha_nam.png"
            }
        }
    ],
    "VinhPhuc": [
        {
            "question": "Tam Đảo là điểm đến nổi tiếng của Vĩnh Phúc, nằm trên dãy núi nào?",
            "options": {
                "A": "Hoàng Liên Sơn",
                "B": "Dãy Tam Đảo",
                "C": "Ba Vì",
                "D": "Pù Luông"
            },
            "answer": "B",
            "culture_card": {
                "province": "VinhPhuc",
                "image_path": "images/cards/tam_dao.png"
            }
        },
        {
            "question": "Vĩnh Phúc có khu danh thắng nào nổi tiếng với chùa Tây Thiên?",
            "options": {
                "A": "Chùa Hương",
                "B": "Tây Thiên",
                "C": "Yên Tử",
                "D": "Tràng An"
            },
            "answer": "B",
            "culture_card": {
                "province": "VinhPhuc",
                "image_path": "images/cards/tay_thien.png"
            }
        },
        {
            "question": "Làng nghề truyền thống nào nổi bật ở Vĩnh Phúc?",
            "options": {
                "A": "Gốm Bát Tràng",
                "B": "Thêu Quất Động",
                "C": "Mộc Bích Chu",
                "D": "Rèn Lý Nhân"
            },
            "answer": "C",
            "culture_card": {
                "province": "VinhPhuc",
                "image_path": "images/cards/lang_moc_bich_chu.png"
            }
        },
        {
            "question": "Vĩnh Phúc thuộc vùng nào của Việt Nam?",
            "options": {
                "A": "Đông Bắc Bộ",
                "B": "Tây Bắc Bộ",
                "C": "Đồng bằng sông Hồng",
                "D": "Bắc Trung Bộ"
            },
            "answer": "C",
            "culture_card": {
                "province": "VinhPhuc",
                "image_path": "images/cards/vinh_phuc.png"
            }
        }
    ],
  "BacGiang": [
    {
      "question": "Loại nông sản nào của Bắc Giang có thương hiệu quốc tế, xuất khẩu sang Nhật Bản, Mỹ, EU và được xem là 'vàng đỏ' của vùng đất Lục Ngạn?",
      "options": {
        "A": "Xoài cát",
        "B": "Mận",
        "C": "Vải thiều",
        "D": "Bưởi"
      },
      "answer": "C",
    "culture_card": {
                "province": "BacGiang",
                "image_path": "images/cards/bacgiang1"}
    },
    {
      "question": "Mỳ Chũ, đặc sản nổi tiếng của Bắc Giang, có điểm đặc biệt gì so với các loại mỳ khác?",
      "options": {
        "A": "Sợi được làm từ khoai tây, có vị bùi",
        "B": "Làm từ gạo bao thai đỏ, sợi dai mềm, khi nấu không bị nát",
        "C": "Sợi mỳ ngắn, trộn với hạt sen để tạo hương thơm",
        "D": "Chỉ có thể làm vào mùa đông vì cần nhiệt độ thấp"
      },
      "answer": "B",
    "culture_card": {
                "province": "HaiPhong", "text": "Mỳ Chũ – Làm từ gạo bao thai đỏ",
                "image_path": "images/cards/bacgiang2"}
    },
    {
      "question": "Chốn tổ của Thiền phái Trúc Lâm, nơi hội tụ tinh hoa Phật giáo Việt Nam, là địa danh nào ở Bắc Giang?",
      "options": {
        "A": "Chùa Bái Đính",
        "B": "Chùa Hương",
        "C": "Tây Yên Tử",
        "D": "Chùa Vĩnh Nghiêm"
      },
      "answer": "C",
    "culture_card": {
                "province": "HaiPhong", "text": "Tây Yên Tử – Trung tâm Phật giáo",
                "image_path": "images/cards/bacgiang3"}
    },
    {
      "question": "Lễ hội nào ở Bắc Giang gắn liền với tinh thần thượng võ, tưởng nhớ phong trào nông dân khởi nghĩa chống thực dân Pháp?",
      "options": {
        "A": "Lễ hội Yên Thế",
        "B": "Lễ hội chùa Hương",
        "C": "Lễ hội Gióng",
        "D": "Lễ hội Lim"
      },
      "answer": "A",
    "culture_card": {
                "province": "HaiPhong", "text": "Lễ hội Yên Thế",
                "image_path": "images/cards/bacgiang4"}
    }
  ],
  "PhuTho": [
    {
      "question": "Phú Thọ được mệnh danh là vùng đất gì?",
      "options": {
        "A": "Thủ đô ngàn năm văn hiến",
        "B": "Cái nôi của văn minh sông Hồng",
        "C": "Cội nguồn dân tộc Việt Nam",
        "D": "Vùng đất thánh địa của Đạo Mẫu"
      },
      "answer": "C",
    "culture_card": {
                "province": "PhuTho", "text": "Phú Thọ – Cội nguồn dân tộc Việt Nam",
                "image_path": "images/cards/phutho1"}
    },
    {
      "question": "Loại hình nghệ thuật nào của Phú Thọ được UNESCO công nhận là Di sản Văn hóa Phi vật thể đại diện của nhân loại?",
      "options": {
        "A": "Ca trù",
        "B": "Quan họ Bắc Ninh",
        "C": "Hát Xoan",
        "D": "Chầu văn"
      },
      "answer": "C",
    "culture_card": {
                "province": "PhuTho",  "text": "Hát Xoan Phú Thọ – Di sản văn hóa phi vật thể",
                "image_path": "images/cards/phutho2"}
    }
  ],
  "ThaiNguyen": [
    {
      "question": "Câu nói sau đây đang nhắc đến đặc sản nào của Thái Nguyên? 'Nước xanh như cốm, hương thơm như hoa, vị đậm đà mà thanh mát, uống một lần nhớ mãi.'",
      "options": {
        "A": "Cà phê Buôn Ma Thuột",
        "B": "Chè Tân Cương",
        "C": "Trà sen Tây Hồ",
        "D": "Trà Shan Tuyết"
      },
      "answer": "B",
    "culture_card": {
                "province": "ThaiNguyen", "text": "Chè Tân Cương – Đặc sản nổi tiếng",
                "image_path": "images/cards/thainguyen1"}
    },
    {
      "question": "Hồ Núi Cốc là một hồ nước ________, được xây dựng nhằm phục vụ tưới tiêu, du lịch và điều tiết nước cho vùng trung du Bắc Bộ.",
      "options": {
        "A": "Tự nhiên",
        "B": "Nhân tạo",
        "C": "Núi lửa cổ tạo thành",
        "D": "Biển hồ"
      },
      "answer": "B",
    "culture_card": {
                "province": "ThaiNguyen", "text": "Hồ Núi Cốc – Hồ nhân tạo phục",
                "image_path": "images/cards/thainguyen2"}
    }
  ],
  "LangSon": [
    {
      "question": "Địa danh nào ở Lạng Sơn được mô tả qua các emoji sau? 🗻👩‍👦💔🌄",
      "options": {
        "A": "Núi Mẫu Sơn",
        "B": "Núi Tô Thị",
        "C": "Động Tam Thanh",
        "D": "Ải Chi Lăng"
      },
      "answer": "B",
    "culture_card": {
                "province": "LangSon",
                "image_path": "images/cards/langson1"}
    },
    {
      "question": "Vào năm 1991, điều gì đã xảy ra với tượng đá nàng Tô Thị trên núi Tô Thị ở Lạng Sơn?",
      "options": {
        "A": "Tượng đá bị phong hóa, tự nhiên sụp đổ",
        "B": "Bị phá hủy do tác động của con người",
        "C": "Được công nhận là di sản quốc gia",
        "D": "Bị sét đánh và vỡ thành nhiều mảnh"
      },
      "answer": "A",
    "culture_card": {
                "province": "LangSon",
                "image_path": "images/cards/langson2"}
    }
  ],
  "TuyenQuang": [
    {
      "question": "Địa danh nào ở Tuyên Quang được mệnh danh là 'Thủ đô Khu giải phóng - Thủ đô Kháng chiến'?",
      "options": {
        "A": "Khu di tích Tân Trào",
        "B": "Thành Tuyên",
        "C": "Động Song Long",
        "D": "Đồi Cọ"
      },
      "answer": "A",
    "culture_card": {
                "province": "LangSon",
                "image_path": "images/cards/tuyenquang1"}
    },
    {
      "question": "Bạn mở một chiếc hộp, bên trong có một vật tròn, mềm, thơm mùi lá chuối, nhân đậu xanh dẻo ngọt. Đây là đặc sản nào của Tuyên Quang?",
      "options": {
        "A": "Bánh gai Chiêm Hóa",
        "B": "Bánh khảo Lâm Bình",
        "C": "Xôi ngũ sắc",
        "D": "Bánh đúc ngô"
      },
      "answer": "A",
    "culture_card": {
                "province": "LangSon",
                "image_path": "images/cards/tuyenquan2"}
    }
  ],
  "CaoBang": [
    {
      "question": "Trong khu di tích Pác Bó có một ngọn núi được đặt theo tên nhà cách mạng vĩ đại. Đó là núi nào?",
      "options": {
        "A": "Núi Các Mác",
        "B": "Núi Lê Nin",
        "C": "Núi Trường Sơn",
        "D": "Núi Cụ Hồ"
      },
      "answer": "B",
    "culture_card": {
                "province": "CaoBang",
                "image_path": "images/cards/caobang1"}
    },
    {
      "question": "Theo kiến thức cùng những hiểu biết của mình, hãy cho biết đâu là ngọn thác lớn, nước đổ trắng xóa, nằm ở biên giới giữa Việt Nam và Trung Quốc?",
      "options": {
        "A": "Thác Datanla",
        "B": "Thác Bản Giốc",
        "C": "Thác Pongour",
        "D": "Thác Dray Nur"
      },
      "answer": "B",
    "culture_card": {
                "province": "CaoBang",
                "image_path": "images/cards/caobang2"}
    }
  ]
}

def get_province_code(province_name):
    return ''.join([w[0].upper() for w in province_name.split()])

def add_id_and_level(data):
    new_data = {}
    for province, questions in data.items():
        easy, hard = [], []
        prefix = get_province_code(province)
        for idx, q in enumerate(questions):
            q["id"] = q.get("id") or f"{prefix}{idx + 1:02d}"
            if "text" in q["culture_card"]:
                del q["culture_card"]["text"]
            level = q.get("level", "Easy")
            if level == "Hard":
                hard.append(q)
            else:
                easy.append(q)
        new_data[province] = {
            "Easy": easy,
            "Hard": hard
        }
    return new_data



# Chuyển đổi dữ liệu
qsbanks = add_id_and_level(raw_qsbanks)
# Ghi file JSON
filepath = os.path.join(data_dir, "qsbanks.json")
with open(filepath, "w", encoding="utf-8") as f:
    json.dump(qsbanks, f, indent=4, ensure_ascii=False)

print(f"Đã tạo file {filepath}")