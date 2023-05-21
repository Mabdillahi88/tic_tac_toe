import gspread
from google.oauth2.service_account import Credentials
import sys
import time
from time import sleep
import os
import random
from validation2 import (get_scoped_credentials, get_gspread_client, get_sheet,
                         login_or_register)

"""
OAuth 2.0 scopes required to access Google Sheets and Drive
"""
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]


def lets_play_noughts_and_crosses():
    player1_username, player2_username = validation2.get_players()


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


"""
Board size for the Noughts and Crosses game
"""
BOARD_SIZE = 3


class NoughtsAndCrossesGame:
    """
    Main game class, handling player turns, board status, and win conditions
    """
    def __init__(self):
        """
        Initialize an empty game board and randomly select the starting player
        """
        self.board = [
            [" " for _ in range(BOARD_SIZE)]
            for _ in range(BOARD_SIZE)
        ]
        self.current_player = random.choice(["X", "O"])

    def switch_player(self):
        """
        Switch the current player
        """
        self.current_player = "O" if self.current_player == "X" else "X"

    def make_move(self, row, column):
        """
        Make a move on the board, if the move is valid
        """
        if (0 <= row < BOARD_SIZE and 0 <= column < BOARD_SIZE
                and self.board[row][column] == " "):
            self.board[row][column] = self.current_player
            return True
        return False

    def check_winner(self):
        """
        Check for a winner or a tie
        """
        for i in range(BOARD_SIZE):
            if (self.board[i][0] == self.board[i][1] ==
                    self.board[i][2] != " "):
                return self.board[i][0]
            if (self.board[0][i] == self.board[1][i] ==
                    self.board[2][i] != " "):
                return self.board[0][i]
        if (self.board[0][0] == self.board[1][1] ==
                self.board[2][2] != " "):
            return self.board[1][1]
        if (self.board[0][2] == self.board[1][1] ==
                self.board[2][0] != " "):
            return self.board[1][1]
        if all(
            self.board[i][j] != " "
            for i in range(BOARD_SIZE)
            for j in range(BOARD_SIZE)
        ):
            return "Tie"
        return None


class NoughtsAndCrossesBoard:
    """
    Class for the game board
    """
    def __init__(self, game):
        """
        Initialize with a reference to the game instance
        """
        self.game = game

    def print_board(self):
        """
        Print the current game board
        """
        for row in self.game.board:
            print("|".join(row))
            print("-" * (BOARD_SIZE * 2 - 1))

    def play_game(self):
        """
        Main game loop: print board, accept player input,
        and check for game end conditions.
        """
        print("Welcome to Noughts and Crosses!")
        self.print_board()

        while True:
            try:
                player_input = input(
                    "Enter the row (0-2) and column (0-2), "
                    "separated by a space: "
                )
"""
Check if the input consists of two numbers from 0-2,
separated by a space.
"""

                row, column = map(int, player_input.split())
                if row not in [0, 1, 2] or column not in [0, 1, 2]:
                    print("Invalid input. Only enter numbers 0, 1 or 2.")
                    continue
                """
Validate if the chosen spot on the board is already occupied.
"""

                if not self.game.make_move(row, column):
                    print("Invalid move. This spot is already occupied.")
                    continue
            except ValueError:
                """
In case of non-integer or non-space separated values, ask
the user to try again.
"""

                print(
                    "Invalid input. Make sure to enter two numbers "
                    "separated by a space."
                )
                continue

            cls()
            self.print_board()

            winner = self.game.check_winner()
            if winner:
                if winner == "Tie":
                    print("It's a tie!")
                else:
                    print(f"Player {winner} wins!")
                break
            self.game.switch_player()


def lets_play_noughts_and_crosses():
    while True:
        print("Welcome to Noughts and Crosses!")
        print("The rules of the game are as follows:")
        print(
            "1. The game is played on a 3x3 grid."
        )
        print(
            "2. Players take turns placing their respective symbols "
            "(X or O) on the grid."
        )
        print(
            "3. The first player to get 3 of their symbols in a row "
            "(horizontally, vertically, or diagonally) wins the game."
        )
        print(
            "4. If all of the spaces on the grid are filled and "
            "no player has won, the game is a tie."
        )
        print("Let's begin!\n")

        game = NoughtsAndCrossesGame()
        board = NoughtsAndCrossesBoard(game)
        board.play_game()

        choice = input("Do you want to play again? (Y/N): ")
        if choice.lower() != "y":
            print("Goodbye!")  # The 'goodbye' message
            break



if __name__ == "__main__":
    """
    Run the Noughts and Crosses game if the script is executed directly
    """
    lets_play_noughts_and_crosses()
