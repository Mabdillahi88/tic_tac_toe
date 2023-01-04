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
    Display a welcome message and the rules of Tic-Tac-Toe
    Prompt the user to choose between logging in or registering
    """
print("Welcome to Tic-Tac-Toe!\n")
print("In this game, you and your opponent will take turns placing X or O on a 3x3 grid. \nThe first player to get 3 of their symbols in a row (horizontally, vertically, or diagonally) wins the game.\n")

login_options = "1) Log in\n2) Register\n"
login_option_selected = input("Please choose an option:\n" + login_options)
separate_line()

# Validate if answer is either 1 or 2
while login_option_selected not in ("1", "2"):
    print("Please choose between one of the two options:")
    login_option_selected = input(login_options)
    separate_line()

# If user wants to log in
if login_option_selected == "1":
    # Connect to Google Sheets
    credentials = Credentials.from_service_account_file(CREDS_FILE, SCOPES)
    client = gspread.authorize(credentials)
    sheet = client.open(SHEET_NAME).sheet1


    # Prompt user for login details
    username = input("Enter your username: ")
    email = input("Enter your email: ")

    # Validate email
    try:
        validate_email(email)
    except EmailNotValidError as e:
        print(e)
        return main_menu()
