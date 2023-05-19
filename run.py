import gspread
from google.oauth2.service_account import Credentials
import sys
import time
from time import sleep
import os
import random
from validation2 import (get_scoped_credentials, get_gspread_client, get_sheet,
                         login_or_register)


# OAuth 2.0 scopes required to access Google Sheets and Drive
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


BOARD_SIZE = 3


class NoughtsAndCrossesGame:
    def __init__(self):
        self.board = [
            [" " for _ in range(BOARD_SIZE)]
            for _ in range(BOARD_SIZE)
        ]
        self.current_player = random.choice(["X", "O"])

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def make_move(self, row, column):
        if (0 <= row < BOARD_SIZE and 0 <= column < BOARD_SIZE
                and self.board[row][column] == " "):
            self.board[row][column] = self.current_player
            return True
        return False

    def check_winner(self):
        for i in range(BOARD_SIZE):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2] != " "):
                return self.board[i][0]
            if (self.board[0][i] == self.board[1][i] == self.board[2][i] != " "):
                return self.board[0][i]
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != " "):
            return self.board[1][1]
        if (self.board[0][2] == self.board[1][1] == self.board[2][0] != " "):
            return self.board[1][1]
        if all(
            self.board[i][j] != " "
            for i in range(BOARD_SIZE)
            for j in range(BOARD_SIZE)
        ):
            return "Tie"
        return None


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
            row, column = map(int, input(
                "Enter the row (0-2) and column (0-2): ").split())
            if not self.game.make_move(row, column):
                print("Invalid move. Try again.")

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
    print("Welcome to Noughts and Crosses!")
    print("The rules of the game are as follows:")
    print("1. The game is played on a 3x3 grid.")
    print("2. Players take turns placing their respective symbols "
          "(X or O) on the grid.")
    print("3. The first player to get 3 of their symbols in a row "
          "(horizontally, vertically, or diagonally) wins the game.")
    print("4. If all of the spaces on the grid are filled and "
          "no player has won, the game is a tie.")
    print("Let's begin!\n")

    game = NoughtsAndCrossesGame()
    board = NoughtsAndCrossesBoard(game)
    board.play_game()


if __name__ == "__main__":
    lets_play_noughts_and_crosses()