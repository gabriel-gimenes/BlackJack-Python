class Card:
    def __init__(self,rank,suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        
        if self.suit == 'C':
            return (self.rank + u'\u2663')

        if self.suit == 'H':
            return (self.rank + u'\u2665')

        if self.suit == 'S':
            return (self.rank + u'\u2660')

        if self.suit == 'D':
            return (self.rank + u'\u2666')

    def getRank(self):
        return self.rank