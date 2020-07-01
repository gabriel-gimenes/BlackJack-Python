class Dealer():
    def __init__(self,dealerHand):
        self.dealerHand = dealerHand

    def setDealerName(self,name):
        self.dealerName = name

    def getDealerName(self):
        return self.dealerName

    def __str__(self):
        return f'\nDealer: {self.dealerHand}' 