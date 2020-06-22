class Hand(object):
    deck = ['AC','AH','AS','AD','2C','2H','2S','2D','3C','3H','3S','3D','4C','4H','4S','4D',
        '5C','5H','5S','5D','6C','6H','6S','6D','7C','7H','7S','7D','8C','8H','8S','8D','9C','9H','9S','9D',
        '10C','10H','10S','10D','JC','JH','JS','JD','QC','QH','QS','QD','KC','KH','KS','KD']

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

            elif cards[0] == '1':
                sum += 10

            else:
                sum += int(cards[0]) 

        return sum
    
    def countCards(self):
        return len(self.card)