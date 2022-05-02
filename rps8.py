import time
import random
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
moves = ['rock', 'paper', 'scissors']


def color_print(message):
    print(f"{Fore.GREEN}{Style.BRIGHT}{message}")
    time.sleep(1.5)


def vaild_input(prompt, choices):
    while True:
        choice = input(f"{Fore.GREEN}{Style.BRIGHT}{prompt}").lower()
        if choice in choices:
            return choice
        color_print("Invaild response. Please try again.\n")


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def __init__(self, moves):
        self.score = 0

    def move(self):
        return random.choice(moves)


class CopycatPlayer(Player):
    def __init__(self, moves):
        self.score = 0
        self.their_move = "None"

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move == "None":
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def __init__(self, moves):
        self.score = 0
        self.my_move = "None"

    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        if self.my_move == moves[0]:
            return moves[1]
        elif self.my_move == moves[1]:
            return moves[2]
        else:
            return moves[0]


class PaperPlayer(Player):
    def __init__(self, moves):
        self.score = 0

    def move(self):
        return 'paper'


class ScissorsPlayer(Player):
    def __init__(self, moves):
        self.score = 0

    def move(self):
        return 'scissors'


class HumanPlayer(Player):
    def __init__(self, moves):
        self.score = 0

    def move(self):
        rps = vaild_input("please chosse rock, paper, or scissors?\n",
                          ["rock", "paper", "scissors"])
        return rps


def beats(self, move1, move2):
    if move1 == move2:
        color_print("It's a tie!\n")
    elif ((move1 == 'rock' and move2 == 'scissors') or
          (move1 == 'scissors' and move2 == 'paper') or
          (move1 == 'paper' and move2 == 'rock')):
        color_print("Player 1 wins!\n")
        self.p1.score += 1
    else:
        color_print("Player 2 wins!\n")
        self.p2.score += 1
    color_print(f"Player 1: {self.p1.score}. Player 2: {self.p2.score}\n")


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        p1 = "None"
        p2 = "None"
        move1 = self.p1.move()
        move2 = self.p2.move()
        color_print(f"Player 1: {move1}  Player 2: {move2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        beats(self, move1, move2)

    def play_again(self):
        color_print("Thank you for playing!\nWould you like to play again?\n")
        another_round = vaild_input("Enter y for Yes.\n"
                                    "Enter n for No.\n", ["y", "n"])
        if another_round == "y\n":
            color_print("New Game will begin soon!\n")
            self.play_game()
        elif another_round == "n\n":
            color_print("Thank you for playing!\nHave a great day!\n")

    def play_game(self):
        color_print("Welcome to Rock, Paper and Scissors project for Udacity!"
                    " Enjoy the Game!\n")
        rounds = vaild_input("How many rounds would you like to play "
                             "1, 3, or 5?\n", ["1", "3", "5"])
        color_print("Game start!\n")
        for round in range(int(rounds)):
            color_print(f"Round {round + 1}:\n")
            self.play_round()
        color_print("Game over!\n")
        if self.p1.score > self.p2.score:
            color_print("Player 1 wins this set!\n")
        elif self.p1.score == self.p2.score:
            color_print("This set is a tie!\n")
        else:
            color_print("Player 2 wins this set!\n")
        self.play_again()


if __name__ == '__main__':
    game = Game(HumanPlayer(Player), RandomPlayer(Player))
    game.play_game()

# Resource https://www.youtube.com/watch?v=xRlN8CFJwAM date used on 4/1/22
# Resource https://www.youtube.com/watch?v=eRZgLI9Sx3c date used on 4/3/22
# Resource https://www.youtube.com/watch?v=-JACmC8kabo date used on 4/3/22
# Resource https://www.youtube.com/watch?v=GhPZHvhvlsk date used on 4/1/22
# Resource https://www.youtube.com/watch?v=u51Zjlnui4Y date used on 4/1/22
# Used adventure game project to help structure a few concepts on 4/8/22
