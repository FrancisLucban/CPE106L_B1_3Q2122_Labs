from dealer import Dealer
from player import Player
from CardObjects import *
import random

class Game:
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = []
        self.fillDeck()

    def fillDeck(self):
        cardNumbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cardSuits = ['C', 'H', 'D', 'S']
        self.deck.clear()
        for number in cardNumbers:
            for suit in cardSuits:
                self.deck.append(Card(number, suit))
        random.shuffle(self.deck)

    def clearScreen(self):
        print("\033[H\033[J", end="")

    def StartMenu(self):
        choice = '\0'
        menuDict = {
            '1': self.beginGame
            }
        while choice != '2':
            self.clearScreen()
            print("WELCOME TO BLACKJACK")
            print("-------------------------")
            print("Input [1] to START GAME")
            print("Input [2] to END GAME")
            print("-------------------------")
            choice = input("Your choice: ")
            menuDict[choice]()
            test = input("Press any key...")

    def bet(self):
        betCash = 0
        self.clearScreen()
        print("Cash: $" + str(self.player.cash))

        while True:
            try:
                print("Your bet value should only be in between $1 and $" + str(self.player.cash))
                betCash =  int(input("Place your bet: $"))
                if(betCash > self.player.cash or betCash <= 0):
                    continue
            except ValueError:
                continue
            else:
                break
        self.player.setBet(betCash)

    def checkEndOfGame(self):
        dealerSum = self.dealer.hand.sumOfCards()
        playerSum = self.player.hand.sumOfCards()
        print("Player: " + str(self.player.hand.sumOfCards()))
        if dealerSum > 21 or playerSum > 21:
            self.clearScreen()
            print("Cash: $" + str(self.player.cash) + "\n")
            print("======[BUST!]======")
            print("[Dealer : " + str(dealerSum) + " | " + "[Player : " + str(playerSum))
            if(dealerSum > 21):
                return 'p'
            if(playerSum > 21):
                return 'd'
        elif dealerSum == 21 or playerSum == 21:
            self.clearScreen()
            print("Cash: $" + str(self.player.cash) + "\n")
            print("======[BLACKJACK!]======")
            print("[Dealer : " + str(dealerSum) + " | " + "[Player : " + str(playerSum))
            if(dealerSum == 21):
                return 'd'
            if(playerSum == 21):
                return 'p'
        return 'f'

    def checkWins(self):
        if self.checkEndOfGame() == 'f':
            return False
        elif self.checkEndOfGame() == 'd':
            return True
        elif self.checkEndOfGame() == 'p':
            self.player.cash += self.player.bet * 2
            return True

    def isGameOngoing(self):
        choice = '\0'
        self.player.hand.addCard(self.deck.pop())
        self.dealer.hand.addCard(self.deck.pop())
        self.player.hand.addCard(self.deck.pop())
        self.dealer.hand.addCard(self.deck.pop())
        self.printCards(False)

        if self.checkWins():
            return False
        else:
            while True:
                print("H = HIT || S = STAND")
                choice = input("Your Input: ")
                self.clearScreen()
                if choice == 'H' or choice == 'h':
                    self.clearScreen()
                    self.player.hand.addCard(self.deck.pop())
                    self.printCards(False)
                    if self.checkWins():
                        return False
                else:
                    break
        return True

    def dealDealer(self):
        if self.dealer.hand.sumOfCards() < self.player.hand.sumOfCards():
            while self.dealer.hand.sumOfCards() < 17:
                self.dealer.hand.addCard(self.deck.pop())
                if self.checkWins():
                    return False
            return True
        else:
            if self.checkWins():
                return False
            return True

    def compareSum(self):
        dealerSum = self.dealer.hand.sumOfCards()
        playerSum = self.player.hand.sumOfCards()
        self.clearScreen()
        print("Cash: " + str(self.player.cash) + "\n")
        if playerSum > dealerSum:
            print("======[YOU WIN!]======")
            print("(Dealer's Hand: " + str(dealerSum) + ")\n")
            return 'p'
        elif dealerSum > playerSum:
            print("======[DEALER WINS!]======")
            print("(Dealer's Hand: " + str(dealerSum) + ")\n")
            return 'd'
        else:
            print("======[DRAW!]======")
            return 'n'

    def printCards(self, endGame):
        print("DECK REMAINING: " + str(len(self.deck)))
        print("---------DEALER---------")
        if(endGame):
            print(str(self.dealer.hand))
        else:
            print(str(self.dealer))
        print("---------PLAYER---------")
        print(str(self.player.hand))

    def beginGame(self):
        self.player.cash = 5000
        choice = '\0'
        while choice != 'n' or choice != 'N':
            if len(self.deck) < 20:
                self.fillDeck()
            self.player.hand.clear()
            self.dealer.hand.clear()
            if self.player.cash > 0:
                self.bet()
            else:
                print("[BANKRUPT! Game Over!]")
                break
            if self.isGameOngoing():
                if self.dealDealer():
                    if self.compareSum() == 'p':
                        self.player.cash += self.player.bet * 2
                        break
                    elif self.compareSum() == 'd':
                        break
                    elif self.compareSum() == 'n':
                        self.player.cash += self.player.bet
                        break

            self.printCards(True)
            print("\n\nCONTINUE?\n[Y] if YES\n[N] if NO\n-----------------------")
            choice = input("Your choice: ")
            self.clearScreen()

def main():
    game = Game()
    game.StartMenu()

main()