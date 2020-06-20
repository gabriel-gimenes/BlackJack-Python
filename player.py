from hand import Hand
from game import Game

class Player(object):
    def __init__(self,balance,playerName,playerHand):
        self.balance = balance
        self.playerName = playerName
        self.playerHand = playerHand

    def player(self):
        print(f'O jogador {self.playerName} tem em suas mãos as cartas {self.playerHand} e possui {self.balance} reais.')

    def setPlayerName(self,name):
        self.playerName = name

    def getPlayerName(self):
        return self.playerName

    def wager(self,money):
        self.bet = money

    def updateBalance(self,earnedmoney):
        self.balance = self.balance - self.wager + earnedmoney

    def getBalance(self):
        return self.balance