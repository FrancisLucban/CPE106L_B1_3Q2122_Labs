class BLACKJACK_CARD:

    cardNumber = '\0'
    cardSuit = '\0'
    cardBlock = False
    firstCard = False

    def __init__(self, cardNumber, cardSuit):

        self.cardNumber = cardNumber
        self.cardSuit = cardSuit

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
            1: "|" + self.cardNumber + "     |",
            2: suitSwitcherTop.get(self.cardSuit),
            3: suitSwitcherBottom.get(self.cardSuit),
            4: "|     " + self.cardNumber + "|",
            5: "`------´"
            }
        for i in range(6):
            cardDisplay += lineSwitcher.get(i) + "\n"

        return cardDisplay
        