from card import Card
class Hand():

    def __init__(self, cards):
        self.cards = cards
        self.cardValues = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'1':10,'J':10,'Q':10,'K':10}

    def addCard(self,card):
        self.cards.append(card)

    def totalHandValue(self):
        sum = 0
        ace = 0
        for card in self.cards:
            if card[0] == 'A':
                ace += 1
            else:
                sum += self.cardValues[card[0]]
        
        for i in range(ace):
            if sum < 11:
                sum += self.cardValues['A'] + 10
            else:
                sum += self.cardValues['A']

        return sum

    def countCards(self):
        return len(self.cards)

    def __str__(self):
        return f'{self.cards}'
