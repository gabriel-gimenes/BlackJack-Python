from hand import Hand

class Player(object):
    def __init__(self,balance,playerName,playerHand):
        self.balance = balance
        self.playerName = playerName
        self.playerHand = playerHand

    def player(self):
        print(f'Jogador: {self.playerName} Cartas: {self.playerHand} Balance: {self.balance}')

    def setPlayerName(self,name):
        self.playerName = name

    def getPlayerName(self):
        return self.playerName

    def setPlayerHand(self,pHand):
        self.playerHand = pHand

    def wager(self,money):
        self.bet = money
        return self.bet

    def updateBalance(self,earnedmoney):
        self.balance += -self.bet + earnedmoney 

    def getBalance(self):
        return self.balance