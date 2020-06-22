import random
from player import Player
from hand import Hand
from dealer import Dealer

class Game(object):
    def __init__(self):
        pass

    def shuffleDeck(self):
        random.shuffle(Hand.deck)

    def playRound(self):
        
        #Acionar os booleanos e iniciar o jogo
        game_on = True
        firstTime = True

        #Jogo começa
        while game_on:
            
            if firstTime:
                print("Welcome to BlackJack Game, let's play!")
                #Embaralhar e dar as cartas
                Game.shuffleDeck(self)
                dealerhand = Hand([Hand.deck.pop(),Hand.deck.pop()])
                playerhand = Hand([Hand.deck.pop(),Hand.deck.pop()])

                playerBusted = False
                dealerBusted = False
                
                #Instanciar as classes
                dealer1 = Dealer('Dealer',dealerhand.card)
                player = Player(200,'Gabriel',playerhand.card)

                #Escolher aposta
                bet = player.wager(int(input("Choose your bet: ")))
                player.updateBalance(0)
                dealer1.dealer()
                print(f'({dealerhand.totalHandValue()})') 
                player.player()
                print(f'({playerhand.totalHandValue()})')

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
                playerhand.addCard(Hand.deck.pop())
                dealer1.dealer()
                print(f'({dealerhand.totalHandValue()})') 
                player.player()
                print(f'({playerhand.totalHandValue()})')

            elif choice == 'D' or choice == 'S':
                if choice == 'D':
                    player.wager(bet)
                    player.updateBalance(0)
                    playerhand.addCard(Hand.deck.pop())
                    dealer1.dealer()
                    print(f'({dealerhand.totalHandValue()})') 
                    player.player()
                    print(f'({playerhand.totalHandValue()})')
                
                else:
                    dealer1.dealer()
                    print(f'({dealerhand.totalHandValue()})') 
                    player.player()
                    print(f'({playerhand.totalHandValue()})')
                
                    
                if dealerhand.totalHandValue() < 17:
                    while dealerhand.totalHandValue() < 17:
                        dealerhand.addCard(Hand.deck.pop())
                    
                    dealer1.dealer()
                    print(f'({dealerhand.totalHandValue()})') 
                    player.player()
                    print(f'({playerhand.totalHandValue()})')

                if dealerhand.totalHandValue() > playerhand.totalHandValue() and dealerhand.totalHandValue() <= 21:
                    print("You lose!")
                    break

                if playerhand.totalHandValue() > dealerhand.totalHandValue() and playerhand.totalHandValue() <= 21:
                    print("You win!")
                    break

                if dealerhand.totalHandValue() > 21 and playerhand.totalHandValue() <= 21:
                    print("Dealer Busted! You win!")
                    dealerBusted = True
                    break

                elif not(playerBusted):
                    print("You busted first!")
                    playerBusted = True

                if playerhand.totalHandValue() > 21 and not(playerBusted):
                    print("You busted!")
                    playerBusted = True
                    break

                if playerhand.totalHandValue() == dealerhand.totalHandValue():
                    print("It's a draw!")
                    break

                dealer1.dealer()
                print(f'({dealerhand.totalHandValue()})') 
                player.player()
                print(f'({playerhand.totalHandValue()})')

            if playerhand.totalHandValue() > 21 and not(playerBusted):
                print("You busted!")
                break

            elif dealerhand.totalHandValue() > 21 and not(dealerBusted):
                print("Dealer busted! You win")
                break