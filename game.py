import random
from player import Player
from hand import Hand
from card import Card
from dealer import Dealer

class Game(object):

    def __init__(self):
        self.deck = ['AC','AH','AS','AD','2C','2H','2S','2D','3C','3H','3S','3D','4C','4H','4S','4D',
        '5C','5H','5S','5D','6C','6H','6S','6D','7C','7H','7S','7D','8C','8H','8S','8D','9C','9H','9S','9D',
        '10C','10H','10S','10D','JC','JH','JS','JD','QC','QH','QS','QD','KC','KH','KS','KD']
    
    def shuffleDeck(self):
        random.shuffle(self.deck)

    def playRound(self):
        dealerhand = Hand([self.deck.pop(-1),self.deck.pop(-1)])
        playerhand = Hand([self.deck.pop(-1),self.deck.pop(-1)])

        Game.shuffleDeck(self)
        print("Welcome to BlackJack Game, let's play!")
        game_on = True
        dealer1 = Dealer('Dealer',dealerhand.card)
        player = Player(200,'Gabriel',playerhand.card)
        dealer1.dealer()
        player.player()
        bet = player.wager(int(input("Choose your bet: ")))
        
        player.updateBalance(0)
        dealer1.dealer()
        player.player()

        if playerhand.totalHandValue() == 21:
            print("BlackJack! You win!")
            game_on = False
        
        elif dealerhand.totalHandValue() == 21:
            print("Dealer got a BlackJack! You lose :(")
            game_on = False

        while game_on:
            if player.playerHand[0][0] == player.playerHand[1][0]:
                choice = input('Hit[H], Stand[S], Split[SS] or Double[D]: ')
            
            else:
                choice = input('Hit[H], Stand[S] or Double[D]: ')

            if choice == 'H':
                playerhand.addCard(self.deck.pop(-1))
            
            elif choice == 'SS':
                player.setPlayerHand([[playerhand.card[0]],[playerhand.card[1]]])

            elif choice == 'D':
                player.wager(bet)
                player.updateBalance()
                playerhand.addCard(self.deck.pop(-1))

            dealer1.dealer()
            player.player()

            if playerhand.bust:
                print("You busted!")
                break

            if dealerhand.bust:
                print("Dealer busted! You win")
                break