class Card:

    def __init__(self, cardNumber, cardSuit):
        valueSwitcher = {
            "A": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J" : 10,
            "Q" : 10,
            "K" : 10
            }
        self.cardNumber = cardNumber
        self.cardSuit = cardSuit
        self.cardValue = valueSwitcher.get(self.cardNumber)

    def __printTopNumber(self):
        if self.cardNumber == "10":
            return ("|" + self.cardNumber + "    |")
        else:
            return ("|" + self.cardNumber + "     |")

    def __printBottomNumber(self):
        if self.cardNumber == "10":
            return ("|    " + self.cardNumber + "|")
        else:
            return ("|     " + self.cardNumber + "|")

    def __str__(self):
        cardDisplay = ""
        suitSwitcherTop = {
            'C': "|  ()  |",
            'H': "| (\\/) |",
            'D': "|  /\\  |",
            'S': "|  /\\  |"
            }

        suitSwitcherBottom = {
            'C': "| ()() |",
            'H': "|  \\/  |",
            'D': "|  \\/  |",
            'S': "| (__) |"
            }

        lineSwitcher = {
            0: ".------.",
            1: self.__printTopNumber(),
            2: suitSwitcherTop.get(self.cardSuit),
            3: suitSwitcherBottom.get(self.cardSuit),
            4: self.__printBottomNumber(),
            5: "`------´"
            }
        for i in range(6):
            cardDisplay += lineSwitcher.get(i) + "\n"

        return cardDisplay

class Hand:

    def __init__(self):
        self.cards = []

    def switchAce(self):
        for card in self.cards:
            if card.cardNumber == "A" and card.cardValue == 11:
                    card.cardValue = 1

    def addCard(self, card):
        if card.cardNumber == "A" and self.sumOfCards() + card.cardValue < 21:
            card.cardValue = 11
        self.cards.append(card)
        if self.sumOfCards() > 21:
            self.switchAce()

    def clear(self):
        self.cards.clear()

    def sumOfCards(self):
        cardSum = 0
        for card in self.cards:
            cardSum += card.cardValue
        return cardSum

    def __str__(self):
        cardsString = ""
        cardLines = []
        if len(self.cards) > 0:
            cardLines = str(self.cards[0]).splitlines()
            tempCardLines = []
            for i in range(1, len(self.cards)):
                tempText = str(self.cards[i])
                tempCardLines = tempText.splitlines()
                for j in range(len(cardLines)):
                    cardLines[j] += " " + tempCardLines[j]

            for i in range(len(cardLines)):
                cardsString += cardLines[i] + "\n"
        return cardsString