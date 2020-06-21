from hand import Hand

class Dealer(object):
    def __init__(self,dealerName,dealerHand):
        self.dealerName = dealerName
        self.dealerHand = dealerHand

    def setDealerName(self,name):
        self.dealerName = name

    def getDealerName(self):
        return self.dealerName

    def dealer(self):
        print()
        print(f'Dealer: {self.dealerName} Cartas: {self.dealerHand}')