from hand import Hand
from game import Game

class Dealer(object):
    def __init__(self,dealerName,dealerHand):
        self.dealerName = dealerName
        self.dealerHand = dealerHand

    def setDealerName(self,name):
        self.dealerName = name

    def getDealerName(self):
        return self.dealerName

    def dealer(self):
        print(f'O {self.dealerName} tem em suas mãos as cartas {self.dealerHand}.')
