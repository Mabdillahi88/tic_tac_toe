import sys
import time
from time import sleep
import os
import random
from colors import Color as Col
import validation as val
from validation2 import 

def logo():
    """
    Display the game logo.
    """
    print(Col.BLUE + "Welcome to:")
    print(" ")
    print(Col.LOGO_Y + "      ____        ____")
    print(Col.LOGO_Y + "     |    |      |    |")
    print(Col.LOGO_R + "     |____|      |____|")
    print(Col.LOGO_Y + "      ____        ____")
    print(Col.LOGO_R + "     |    |      |    |")
    print(Col.LOGO_Y + "     |____|      |____|")
    print(" ")
    print(" ")
    print(Col.BLUE + "                                        Tic Tac Toe")
    print(" ")
    print(" ")
    time.sleep(1)

print("Get ready to play Tic Tac Toe!")


def cls():
    """
    Clear the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def separate_line():
    """
    Print a line separator.
    """
    print("\n" + "-"*30 + "\n")

def main_menu():
    """
    Display the main menu and prompt the user to choose between logging in or registering.
    """
    print("Welcome to Tic-Tac-Toe!\n")
  
    options = "1) Log in\n2) Register\n"
    selection = input("Please choose an option:\n" + options)
    separate_line()

    # Validate the user's input to make sure it is either 1 or 2
    while selection not in ("1", "2"):
        print("Please choose between one of the two options:")
        selection = input(options)
        separate_line()
    
    # If the user chooses to log in, call the login_users function
    if selection == "1":
        get_login_and_email()
  
    # If the user chooses to register, call the register_players function
    elif selection == "2":
        register_new_user()

    return selection



def lets_play_tic_tac_toe():
  print("Welcome to Tic Tac Toe!")
  print("The rules of the game are as follows:")
  print("1. The game is played on a 3x3 grid.")
  print("2. Players take turns placing their respective symbols (X or O) on the grid.")
  print("3. The first player to get 3 of their symbols in a row (horizontally, vertically, or diagonally) wins the game.")
  print("4. If all of the spaces on the grid are filled and no player has won, the game is a draw.")
  print("Let's begin!")
  separate_line()


import random

BOARD_SIZE = 3

class NoughtsAndCrossesGame:
    def __init__(self):
        self.board = [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.current_player = random.choice(["X", "O"])

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def make_move(self, row, column):
        if self.board[row][column] == " ":
            self.board[row][column] = self.current_player
            return True
        return False

    def check_winner(self):
        for i in range(BOARD_SIZE):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]  # Winner in row i
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]  # Winner in column i
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[1][1]  # Winner in top-left to bottom-right diagonal
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[1][1]  # Winner in top-right to bottom-left diagonal
        if all(self.board[i][j] != " " for i in range(BOARD_SIZE) for j in range(BOARD_SIZE)):
            return "Tie"  # Game is a tie
        return None  # No winner or tie

class NoughtsAndCrossesBoard:
    def __init__(self, game):
        self.game = game

    def print_board(self):
        for row in self.game.board:
            print("|".join(row))
            print("-" * (BOARD_SIZE * 2 - 1))

    def play_game(self):
        print("Welcome to Noughts and Crosses!")
        self.print_board()

        while True:
            row = int(input("Enter the row (0-2): "))
            column = int(input("Enter the column (0-2): "))

            if self.game.make_move(row, column):
                winner = self.game.check_winner()
                if winner:
                    self.print_board()
                    if winner == "Tie":
                        print("It's a tie!")
                    else:
                        print(f"Player {winner} wins!")
                    break

            self.print_board()
            self.game.switch_player()

# Start the game
game = NoughtsAndCrossesGame()
board = NoughtsAndCrossesBoard(game)
board.play_game()

