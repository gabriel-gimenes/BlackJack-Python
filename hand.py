class Hand(object):
    def __init__(self, card):
        self.card = card

    def addCard(self,card):
        self.card += [card]

    def totalHandValue(self):
        sum = 0
        for cards in self.card:
            if cards[0] == 'J' or cards[0] == 'K' or cards[0] == 'Q':
                sum += 10
            
            elif cards[0] == 'A':
                if sum > 10:
                    sum += 1
                else:
                    sum += 11

            else:
                sum += int(cards[0]) 

        return sum
    
    def countCards(self):
        return len(self.card)

    def bust(self):
        return self.totalHandValue() > 21