import re
import gspread
from google.oauth2.service_account import Credentials
import time
from email_validator import validate_email, EmailNotValidError
import time
from Colors import Color as Col
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

def main_menu():
    """
    Prompt the user to choose between logging in or registering
    """
    print("Welcome to Tic-Tac-Toe!\n")
  
    options = "1) Log in\n2) Register\n"
    selection = input("Please choose an option:\n" + options)
    separate_line()

    # Validate if answer is either 1 or 2
    while selection not in ("1", "2"):
        print("Please choose between one of the two options:")
        selection = input(options)
        separate_line()
    
    if selection == "1":
        add_new_users()
  

    elif selection == "2":
        lets_play_tic_tac_toe()

    return selection

def lets_play_tic_tac_toe():
  print("Welcome to Tic Tac Toe!")
  print("The rules of the game are as follows:")
  print("1. The game is played on a 3x3 grid.")
  print("2. Players take turns placing their respective symbols (X or O) on the grid.")
  print("3. The first player to get 3 of their symbols in a row (horizontally, vertically, or diagonally) wins the game.")
  print("4. If all of the spaces on the grid are filled and no player has won, the game is a draw.")
  print("Let's begin!")

lets_play_tic_tac_toe()
