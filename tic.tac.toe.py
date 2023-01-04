import re
import gspread
from google.oauth2.service_account import Credentials
import time
from email_validator import validate_email, EmailNotValidError
import time
from colors import Color as Col
import os

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS_FILE = 'creds.json'
SHEET_NAME = 'Tic_tac_toe'

def logo():
    """
    Display game name
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
    os.system("cls" if os.name == "nt" else "clear")


def separate_line():
    print("\n" + "-"*30 + "\n")

def main_menu() -> str:
"""
Display a welcome message and the rules of Tic-Tac-Toe
Prompt the user to choose between logging in or registering
"""
print("Welcome to Tic-Tac-Toe!\n")
print("In this game, you and your opponent will take turns placing X or O on a 3x3 grid. \nThe first player to get 3 of their symbols in a row (horizontally, vertically, or diagonally) wins the game.\n")


