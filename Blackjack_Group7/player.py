from CardObjects import Hand

class Player:

    def __init__(self):
        self.hand = Hand()
        self.cash = 5000
        self.bet = 0

    def setBet(self, betValue):
        self.bet = 0
        self.cash -= betValue
        self.bet += betValue