from dealer import Dealer
from player import Player
from CardObjects import *
import random
from os import system, name
import time
import sys

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
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def StartMenu(self):
        choice = '\0'
        while True:
            self.clearScreen()
            print("WELCOME TO BLACKJACK")
            print("-------------------------")
            print("Input [1] to START GAME")
            print("Input [2] to END GAME")
            print("-------------------------")
            choice = input("Your choice: ")
            if choice == '1':
                self.player.cash = 5000
                while True:
                    if(self.beginGame() == False):
                        break

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
        if int(len(self.player.hand.cards)) == 5 and playerSum <= 21:
            self.clearScreen()
            self.printCards(True)
            print("Cash: $" + str(self.player.cash) + "\n")
            print("======[FIVE CARD CHARLIE!]======")
            return 'c'
        elif dealerSum > 21 or playerSum > 21:
            self.clearScreen()
            self.printCards(True)
            print("Cash: $" + str(self.player.cash) + "\n")
            print("======[BUST!]======")
            print("[Dealer : " + str(dealerSum) + " | " + "[Player : " + str(playerSum) + "]")
            if(dealerSum > 21):
                return 'p'
            if(playerSum > 21):
                return 'd'
        elif dealerSum == 21 or playerSum == 21:
            self.clearScreen()
            self.printCards(True)
            print("Cash: $" + str(self.player.cash) + "\n")
            print("======[BLACKJACK!]======")
            print("[Dealer : " + str(dealerSum) + " | " + "[Player : " + str(playerSum) + "]")
            if(dealerSum == 21):
                return 'd'
            if(playerSum == 21):
                return 'p'
        return 'f'

    def checkWins(self):
        if self.checkEndOfGame() == 'f':
            return False
        elif self.checkEndOfGame() == 'd':
            print("You lost $" + str(self.player.bet))
            input("Press Enter to continue...")
            return True
        elif self.checkEndOfGame() == 'p':
            self.player.cash += self.player.bet * 2
            print("You won $" + str(self.player.bet * 2))
            input("Press Enter to continue...")
            return True
        elif self.checkEndOfGame() == 'c':
            self.player.cash += self.player.bet * 5
            print("You won $" + str(self.player.bet * 5))
            input("Press Enter to continue...")
            return True

    def isGameOngoing(self):
        gameChoice = '\0'
        self.player.hand.addCard(self.deck.pop())
        self.dealer.hand.addCard(self.deck.pop())
        self.player.hand.addCard(self.deck.pop())
        self.dealer.hand.addCard(self.deck.pop())
        self.printCards(False)

        if self.checkWins():
            return False
        else:
            while True:
                print("Your Bet: $" + str(self.player.bet))
                print("Current Sum: " + str(self.player.hand.sumOfCards()))
                print("H = HIT || S = STAND")
                gameChoice = input("Your Input: ")
                self.clearScreen()
                if gameChoice == 'H' or gameChoice == 'h':
                    self.clearScreen()
                    self.player.hand.addCard(self.deck.pop())
                    self.printCards(False)
                    if self.checkWins():
                        return False
                elif gameChoice == 'S' or gameChoice == 's':
                    break
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
        if playerSum > dealerSum:
            self.printCards(True)
            print("======[YOU WIN!]======")
            print("[Dealer : " + str(dealerSum) + " | " + "[Player : " + str(playerSum) + "]")
            return 'p'
        elif dealerSum > playerSum:
            self.printCards(True)
            print("======[DEALER WINS!]======")
            print("[Dealer : " + str(dealerSum) + " | " + "[Player : " + str(playerSum) + "]")
            return 'd'
        else:
            self.printCards(True)
            print("======[DRAW!]======")
            print("[Dealer : " + str(dealerSum) + " | " + "[Player : " + str(playerSum) + "]")
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
        continueChoice = '\0'
        while True:
            if len(self.deck) < 20:
                self.fillDeck()
            self.player.hand.clear()
            self.dealer.hand.clear()
            if self.player.cash > 0:
                self.bet()
            else:
                print("[BANKRUPT! Game Over!]")
                print("\n\nCONTINUE?\n[Y] if YES\n[N] if NO\n-----------------------")
                continueChoice = 'n'
                continueChoice = input("Your choice: ")
                if continueChoice != 'n' or continueChoice != 'N':
                    self.clearScreen()
                    self.player.cash = 5000
                    return True
                else:
                    self.clearScreen()
                    return False
            if self.isGameOngoing():
                if self.dealDealer():
                    if self.compareSum() == 'p':
                        self.player.cash += self.player.bet * 2
                        input("Press Enter to continue...")
                        return True
                    elif self.compareSum() == 'd':
                        input("Press Enter to continue...")
                        return True
                    elif self.compareSum() == 'n':
                        self.player.cash += self.player.bet
                        input("Press Enter to continue...")
                        return True
def main():
    game = Game()
    game.StartMenu()

main()