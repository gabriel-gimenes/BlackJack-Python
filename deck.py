import random
class Deck():
    suits = ('C', 'H', 'S', 'D')
    ranking = ('A', '2', '3', '4', '5', '6', '7', '8','9', '10', 'J', 'Q', 'K')

    def __init__(self):
        self.deck = []

        for rank in self.ranking:
            for suit in self.suits:
                self.deck += [rank + suit]

    def show(self):
        print(self.deck)

    def shuffleDeck(self):
        random.shuffle(self.deck)

    def drawCard(self):
        return self.deck.pop()