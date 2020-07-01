import random
from player import Player
from hand import Hand
from dealer import Dealer
from deck import Deck
from card import Card

class Game():
    def __init__(self):
        pass

    def playRound(self):
        
        #Acionar os booleanos e iniciar o jogo
        game_on = True
        firstTime = True

        #Jogo começa
        while game_on:
            
            if firstTime:
                print("Welcome to BlackJack Game, let's play!")
                #Embaralhar e dar as cartas
                deck = Deck()
                deck.shuffleDeck()
                dealerhand = Hand([deck.drawCard(),deck.drawCard()])
                playerhand = Hand([deck.drawCard(),deck.drawCard()])
                
                #Instanciar as classes
                dealer = Dealer(dealerhand.cards)
                player = Player(200,'Gabriel',playerhand.cards)

                #Escolher aposta
                bet = int(input("Choose your bet: "))

                print(dealer) 
                print(player)

                if playerhand.totalHandValue() == 21:
                    print("BlackJack! You win!")
                    break
        
                if dealerhand.totalHandValue() == 21:
                    print("Dealer got a BlackJack! You lose :(")
                    break

                choice = input('Hit[H], Stand[S], or Double[D]: ')
                firstTime = False
            else:
                choice = input('Hit[H], Stand[S]: ')

            if choice == 'H':
                playerhand.addCard(deck.drawCard())
                print(dealer)
                print(player)

            elif choice == 'D' or choice == 'S':
                if choice == 'D':
                    player.wager(bet)
                    playerhand.addCard(deck.drawCard())
                    
                if dealerhand.totalHandValue() < 17:
                    while dealerhand.totalHandValue() < 17:
                        dealerhand.addCard(deck.drawCard())
                    
                    print(dealer)
                    print(player)

                if dealerhand.totalHandValue() <= 21:
                    if dealerhand.totalHandValue() > playerhand.totalHandValue():
                        print("You lose!")
                        break

                    elif playerhand.totalHandValue() <= 21:
                        print("You beat the dealer! You win!")
                        break

                else:
                    if playerhand.totalHandValue() > 21:
                        print("You busted, dealer wins!")
                        break
                    else:
                        print("Dealer Busted! You win!")
                        break

                if playerhand.totalHandValue() == dealerhand.totalHandValue():
                    print("It's a draw!")
                    break

                print(dealer)
                print(player)