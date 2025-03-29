from Project.Models.Culturecard import CultureCard
from Project.Models.Player import Player

card1 = CultureCard("DienBien", "Đồi A1 – Chiến thắng", "images/cards/doi_a1.png")
player = Player("teo", "123")
player.add_card(card1)

print(player)
