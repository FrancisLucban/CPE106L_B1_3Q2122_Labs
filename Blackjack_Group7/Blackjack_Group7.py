from Classes import BLACKJACK_CARD

cards = [BLACKJACK_CARD('3', 'H'), BLACKJACK_CARD('Q', 'D'), BLACKJACK_CARD('A', 'S')]

def multipleCardPrint(cards):
    cardsString = ""
    if len(cards) > 0:
        cardLines = str(cards[0]).splitlines()
        tempCardLines = []
        for i in range(1, len(cards)):
            tempText = str(cards[i])
            tempCardLines = tempText.splitlines()
            for j in range(len(cardLines)):
                cardLines[j] += " " + tempCardLines[j]

        for i in range(len(cardLines)):
            cardsString += cardLines[i] + "\n"
    print(cardsString)


multipleCardPrint(cards)