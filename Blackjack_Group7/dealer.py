from CardObjects import Hand

class Dealer:

    def __init__(self):
        self.hand = Hand()

    def __str__(self):
        cardString = ""
        cardLines = []
        cardLines = str(self.hand.cards[0]).splitlines()
        cardLines[0] += ".------."
        cardLines[1] += "|?     |"
        cardLines[2] += "|      |"
        cardLines[3] += "|      |"
        cardLines[4] += "|     ?|"
        cardLines[5] += "`------´"
        cardsString = ""
        for i in range(len(cardLines)):
            cardsString += cardLines[i] + "\n"
        return cardsString
