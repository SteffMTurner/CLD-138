
from Deck import Deck
from Player import Player
from WarGame import WarCardGame

player = Player("You", Deck(is_empty=True))
computer = Player("Computer", Deck(is_empty=True), is_Computer=True)
deck = Deck(is_empty=True)
game = WarCardGame(player, computer, deck)
game.print_welcome()
while not game.check_game_over():
  game.start_battle()
  game.print_stats()
  answer = input("\n Ready for next round? \nPress Enter to continue, or x to stop!")
  if answer.lower() == "x":
    break