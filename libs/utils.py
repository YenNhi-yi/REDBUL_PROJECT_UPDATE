import random

def shuffle_list(items):
    """Xáo trộn thứ tự các phần tử trong danh sách"""
    random.shuffle(items)
    return items

def get_next_region(current_region, regions_order):
    """
    Trả về tên miền tiếp theo trong danh sách `regions_order`
    """
    try:
        idx = regions_order.index(current_region)
        return regions_order[idx + 1] if idx + 1 < len(regions_order) else None
    except ValueError:
        return None

def validate_username(username):
    """
    Kiểm tra tên người dùng: phải từ 3–16 ký tự, không chứa dấu cách/ký tự đặc biệt
    """
    return username.isalnum() and 3 <= len(username) <= 16

def check_completed_region(player, region_name, regions_data):
    """
    Kiểm tra xem người chơi đã thu thập đủ thẻ văn hóa cho miền `region_name` chưa.
    """
    required_provinces = regions_data.get(region_name, [])
    collected_provinces = [card['province'] for card in player.collected_cards]
    return all(province in collected_provinces for province in required_provinces)
