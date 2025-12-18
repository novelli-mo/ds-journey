from numpy import random
from colorama import Fore, Back, Style, init
from itertools import cycle
import time

class Guesser:
    def __init__(self):
        self.secret = random.randint(1, 100)
    
    def asks_for_number(self):
        return int(input("What's your guess? "))

    def guesser(self, guess):
        if guess < self.secret:
            print("Too low")
            return False
        elif guess > self.secret:
            print("Too high")
            return False
        elif guess == self.secret:
            print("Correct!")
            return True
        else:
            print("Oops!")
            return True
    
    def rainbow_print(self,text, delay=0.002):
        colors = cycle([Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA])
        for char in text:
            print(next(colors) + Style.BRIGHT + char, end="", flush=True)
            time.sleep(delay)
        print()

    def confetti(self):
        colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.MAGENTA]
        symbols = ["*", "✦", "✺", "✹", "❇", "❈"]

        for _ in range(8):
            line = ""
            for _ in range(60):
                line += random.choice(colors) + random.choice(symbols)
            print(line)
            time.sleep(0.05)

    def win(self):

        self.confetti()
        banner = [
            "  ██████  ██████  ███    ██  ██████  ██████   █████  ███████ ███████ ",
            " ██      ██    ██ ████   ██ ██       ██   ██ ██   ██   ███       ██  ",
            " ██      ██    ██ ██ ██  ██ ██   ███ ██████  ███████   ███    █████  ",
            " ██      ██    ██ ██  ██ ██ ██    ██ ██   ██ ██   ██   ███   ██      ",
            "  ██████  ██████  ██   ████  ██████  ██   ██ ██   ██   ███  ███████ ",
        ]

        print("\n")
        for line in banner:
            self.rainbow_print(line)

        print()
        self.rainbow_print("YOU GUESSED THE NUMBER!", delay=0.01)
        self.rainbow_print("Absolute legend. The computer never stood a chance.\n", delay=0.01)
    
    def start(self):
        guess = self.asks_for_number()
        correct = self.guesser(guess)

        if correct:
            self.win()
        elif guess == 'EXIT':
            print('Goodbye!')
        else:
            self.start()  

print('Welcome to the guessing game! I will choose a number from 1-100. Try to guess it.')
print('Type EXIT to exit the game.')

game = Guesser()
game.start()