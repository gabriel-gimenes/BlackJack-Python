from hand import Hand
class Player():
    def __init__(self,balance,playerName,playerHand):
        self.balance = balance
        self.playerName = playerName
        self.playerHand = playerHand

    def __str__(self):
        self.hand = Hand(self.playerHand)
        return f'{self.playerName}: {self.playerHand} ({self.hand.totalHandValue()})'

    def setPlayerName(self,name):
        self.playerName = name

    def getPlayerName(self):
        return self.playerName

    def wager(self,chips):
        self.balance -= chips 

    def getBalance(self):
        return self.balance