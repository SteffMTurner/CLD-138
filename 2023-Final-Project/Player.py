class Player:
  def __init__ (self, name, deck, is_Computer=False):
    self._name = name
    self._deck = deck
    self._is_Computer = is_Computer

    @property
    def is_Computer(self):
      return self._is_computer
    @property
    def deck(self):
      return self.deck
  
    def has_empty_deck(self):
      return self._deck.size == 0
    def draw_card(self):
      if self.has_empty_deck():
        return self._deck.draw()
      else:
       None
    def add_card(self, card):
      self._deck.add(card)