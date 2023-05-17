import gspread
from google.oauth2.service_account import Credentials
import sys
import time
from time import sleep
import os
import random
from validation2 import get_scoped_credentials, get_gspread_client, get_sheet, login_or_register


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
        self.board = [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.current_player = random.choice(["X", "O"])

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def make_move(self, row, column):
        if 0 <= row < BOARD_SIZE and 0 <= column < BOARD_SIZE and self.board[row][column] == " ":
            self.board[row][column] = self.current_player
            return True
        return False

    