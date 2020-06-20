from hand import Hand
from game import Game
from card import Card
from dealer import Dealer
from player import Player

game = Game()
game.shuffleDeck()
dealer = Dealer('Dealer', game.deck.pop(-1))
player = Player(200,'Gabriel',game.deck.pop(-1))