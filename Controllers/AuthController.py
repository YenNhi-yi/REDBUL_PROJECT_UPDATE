from Project.Models.Player import Player
from Project.libs.Dataconnector import DataConnector


class AuthController:
    def __init__(self):
        self.dc = DataConnector()
        self.current_player = None

    def login(self, username, password):
        for player in self.dc.players:
            if player.username == username and player.password == password:
                self.current_player = player
                return True
        return False

    def register(self, username, password, confirm_password):
        if not username or not password:
            return False, "Tên đăng nhập và mật khẩu không được để trống."

        if password != confirm_password:
            return False, "Mật khẩu không khớp!"

        if self.dc.get_player_by_username(username):
            return False, "Tên người dùng đã tồn tại!"

        new_player = Player(username, password)
        self.dc.players.append(new_player)
        self.dc.save_players()
        self.current_player = new_player
        return True, "Đăng ký thành công!"

    def get_current_player(self):
        return self.current_player

    def save_players(self):
        self.dc.save_players()
