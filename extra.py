"""
A tic-tac-toe game built with Python and Tkinter.
"""

import tkinter as tk
import os
import time
from itertools import cycle
from tkinter import font
from typing import NamedTuple

class Player(NamedTuple):
    label: str
    color: str

class Move(NamedTuple):
    row: int
    col: int
    label: str = ""

BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="green"),
)

def display_logo():
    """
    Display game name and rules
    """
    print("Welcome to Tic Tac Toe!")
    print(" ")
    print("The goal of the game is to get three of your symbols in a row (horizontally, vertically, or diagonally) before your opponent does.")
    print("You will be asked to enter the row and column where you want to place your symbol (X or O) on the board.")
    print(" ")
    time.sleep(1)

def clear_console():
    """
    Clear the console
    """
    os.system("cls" if os.name == "nt" else "clear")

def display_separator():
    """
    Print '-' lines to separate messages
    """
    print(" ")
    print("- "*30)
    print(" ")
def main_menu() -> str:
    """
    The program will first show two possible options of the game
    User can select to view game rules or start game
    """
    display_logo()
    time.sleep(1)
    print("What would you like to do?")
    start_options = "1) View game rules\n2) Play game\n"
    start_option_selected = input(start_options)
    display_separator()

    # Validate if answer is either 1 or 2
    while start_option_selected not in ("1", "2"):
        print("Please choose between one of the two options:")
        start_option_selected = input(start_options)
        display_separator()

    if start_option_selected == "1":
        clear_console()
        display_logo()
        game_rules()

    elif start_option_selected == "2":
        start_game()

    return start_option_selected
main_menu()


import os
import time

def clear_screen():
  """
  Clear the console screen
  """
  os.system("cls" if os.name == "nt" else "clear")

def display_game_title():
  """
  Display the game title and rules
  """
  clear_screen()
  print("Welcome to Tic Tac Toe!")
  print(" ")
  print("The goal of the game is to get three of your symbols in a row (horizontally, vertically, or diagonally) before your opponent does.")
  print("You will be asked to enter the row and column where you want to place your symbol (X or O) on the board.")
  print(" ")
  time.sleep(1)

display_game_title()


import random
import sys
import time
import os
import tkinter as tk
import copy

import time
from colors import Color as Col
import os
import time


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
    print("In this game, you and your opponent will take turns placing X or O on a 3x3 grid. The first player to get 3 of their symbols in a row (horizontally, vertically, or diagonally) wins the game.\n")
    login_options = "1) Log in\n2) Register\n"
    login_option_selected = input("Please choose an option:\n" + login_options)
    separate_line()

    # Validate if answer is either 1 or 2
    while login_option_selected not in ("1", "2"):
        print("Please choose between one of the two options:")
        login_option_selected = input(login_options)
        separate_line()

def login_menu() -> Tuple[str, str]:
    """
    Prompt the user to enter their username and email address
    Return the username and email as a tuple
    """
    username = input("Please enter your username: ")
    email = input("Please enter your email address: ")
    return username, email


def main_menu() -> str:
    """
    Display a welcome message and the rules of Tic-Tac-Toe
    Prompt the user to choose between logging in or registering
    """
    print("Welcome to Tic-Tac-Toe!\n")
    print("In this game, you and your opponent will take turns placing X or O on a 3x3 grid. The first player to get 3 of their symbols in a row (horizontally, vertically, or diagonally) wins the game.\n")
    login_options = "1) Log in\n2) Register\n"
    login_option_selected = input("Please choose an option:\n" + login_options)
    separate_line()

    # Validate if answer is either 1 or 2
    while login_option_selected not in ("1", "2"):
        print("Please choose between one of the two options:")
        login_option_selected = input(login_options)
        separate_line()

    # If the user selected "Log in", prompt them for their username and email
    if login_option_selected == "1":
        username, email = login_menu()
    # If the user selected "Register", create a new account for them
    else:
        username, email = login_menu()
        create_account(username, email)



        def main_menu():
    """
    Display a welcome message and the rules of Tic-Tac-Toe
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



import re
import gspread
from google.oauth2.service_account import Credentials
import time
from email_validator import validate_email, EmailNotValidError

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS_FILE = 'creds.json'
SHEET_NAME = 'Tic_tac_toe'

def get_scoped_credentials(scopes):
    creds = Credentials.from_service_account_file(CREDS_FILE)
    return creds.with_scopes(scopes)

def get_gspread_client(creds):
    return gspread.authorize(creds)

def get_sheet(client, sheet_name):
    return client.open(sheet_name)

def add_user_data_to_sheet(sheet, username, email):
    # Get the first sheet in the workbook
    worksheet = sheet.get_worksheet(0)

    # Check if the headings are present in the first row
    if worksheet.row_values(1) != ["Username", "Email"]:
        # Insert the headings if they are not present
        worksheet.insert_row(["Username", "Email"], 1)

    # Get the values in the first and second columns of the sheet
    usernames = worksheet.col_values(1)
    emails = worksheet.col_values(2)

    while True:
        # Check if the username and email address already exist in the sheet
        if username in usernames:
            print('Error: username already exists')
            username = input("Enter a different username: ")
            continue
        if email in emails:
            print('Error: email address already exists')
            email = input("Enter a different email address: ")
            continue

        # If the username and email are not in the sheet, append the data and exit the loop
        worksheet.append_row([username, email])
        print('User data added successfully')
        break


def main():
    # Get the scoped credentials, client, and sheet
    scoped_creds = get_scoped_credentials(SCOPES)
    client = get_gspread_client(scoped_creds)
    sheet = get_sheet(client, SHEET_NAME)

    for player_num in range(1, 3):
        # Set a flag to indicate if the input is valid
        input_valid = False

        # Run the loop until the input is valid
        while not input_valid:
            # Ask the user for their username and email
            username = input(f'Enter the username for player {player_num}: ')
            email = input(f'Enter the email address for player {player_num}: ')

            # Validate the user input
            if len(username) < 3:
                print('Error: username must be at least 3 characters long')
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                print('Error: email address is not valid')
            else:
                input_valid = True

        # Add the user data to the sheet
        add_user_data_to_sheet(sheet, username, email)

if __name__ == '__main__':
    main()



import re
import gspread
from google.oauth2.service_account import Credentials
import time
from email_validator import validate_email, EmailNotValidError

from datetime import datetime
from typing import NamedTuple

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


class TicTacToeGame:
    def __init__(self, player1, player2, result, duration, date_played):
        self.player1 = player1
        self.player2 = player2
        self.result = result
        self.duration = duration
        self.date_played = date_played

player1 = Player("player1@example.com", "X")
player2 = Player("player2@example.com", "O")
game = TicTacToeGame(player1, player2, "win", 3600, datetime.now())

results = {
    "X": {"wins": 0, "losses": 0, "draws": 0},
    "O": {"wins": 0, "losses": 0, "draws": 0}
}

if game.result == "win":
    results[game.player1.label]["wins"] += 1
    results[game.player2.label]["losses"] += 1
elif game.result == "loss":
    results[game.player1.label]["losses"] += 1



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
        return None

    # Check if login details are present in the sheet
    try:
        cell = sheet.find(username)
        row = cell.row
        stored_email = sheet.cell(row, 2).value
        if stored_email == email:
            # Login successful
            print("Welcome back, {}!".format(username))
            return None
        else:
            # Incorrect email
            print("Incorrect email for the given username. Please try again or register a new account.")
            return main_menu()
    except gspread.exceptions.CellNotFound:
        # Incorrect username
        print("Username not found. Please try again or register a new account.")
        return None


# If user wants to register
elif login_option_selected == "2":
    # Prompt user for registration details
    username = input("Enter a new username: ")
    email = input("Enter your email: ")

    # Validate email
    try:
        validate_email(email)
    except EmailNotValidError as e:
        print(e)
        return None

    # Connect to Google Sheets
    credentials = Credentials.from_service_account_file(CREDS_FILE, SCOPES)
    client = gspread.authorize(credentials)
    sheet = client.open(SHEET_NAME).sheet1

    # Check if username is already taken
    try:
        cell = sheet.find(username)
        print("The chosen username is already taken. Please try a different one.")
        return None
    except gspread.exceptions.CellNotFound:
        # Add new user to the sheet
        sheet.append_row([username, email])
        print("Your account has been successfully registered!")
        return None

def main():
    # Display the logo
    logo()
    # Display the main menu
    username = main_menu()

# Run the main function
if name == "main":
    main()


import gspread
from google.oauth2.service_account import Credentials
from email_validator import validate_email, EmailNotValidError


# Set the credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open the sheet and worksheet
sheet = GSPREAD_CLIENT.open("Tic_tac_toe").worksheet("logins_register")

# Function to get login and email from user
def get_login_and_email():
    login = input("Enter your login: ")
    email = input("Enter your email: ")
    return login, email

# Function to check if login and email are registered
def is_login_and_email_registered(login, email):
    logins = sheet.col_values(1)  # Get all logins from the first column
    emails = sheet.col_values(2)  # Get all emails from the second column
    return login in logins and email in emails

# Get the login and email for the user
login, email = get_login_and_email()

if is_login_and_email_registered(login, email):
    # Find the row where the login and email appear
    cell = sheet.find(login)
    login_row = cell.row
    # Retrieve the name and score from the row
    name = sheet.row_values(login_row)[0]
    score = int(sheet.row_values(login_row)[2])
    print(f"\nHello {name}!\n")
else:
    print("Login and email not registered. Please try again.")

def get_username_and_email():
    username = input("Enter your desired username: ")
    email = input("Enter your email: ")
    return username, email


def is_username_registered(username):
    usernames = sheet.col_values(1) # Get all usernames from the first column
    return username in usernames

def is_email_registered(email):
    emails = sheet.col_values(2) # Get all emails from the second column
    return email in emails


def register_new_user():
    # Get username and email from user
    username, email = get_username_and_email()
    if not username:
        print("Username cannot be empty. Please enter a valid username.")
    return

    if not email:
        print("Email cannot be empty. Please enter a valid email.")
        return


    # Validate that the username is not already registered
    if is_username_registered(username):
        print("Username already exists. Please choose a different username.")
        return

    # Validate that the email is not already registered
    if is_email_registered(email):
        print("Email already registered. Please use a different email.")
        return

    # Validate that the email is in a valid format
    try:
        validated_email = validate_email(email)
        email = validated_email.email
    except EmailNotValidError as e:
        print("Invalid email format. Please enter a valid email.")
        return

    #Add the new user to the sheet

    sheet.append_row([username, email])
    print("Successfully registered new user.")

def get_username_and_email():
   username = input("Enter your desired username: ")
   email = input("Enter your email: ")
   return username, email

def is_username_registered(username):
   usernames = sheet.col_values(1) # Get all usernames from the first column
   return username in usernames

def is_email_registered(email):
   emails = sheet.col_values(2) # Get all emails from the second column
   return email in emails

   register_new_user()


import re
import gspread
from google.oauth2.service_account import Credentials
import time
from email_validator import validate_email, EmailNotValidError

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS_FILE = 'creds.json'
SHEET_NAME = 'Tic_tac_toe'

def get_scoped_credentials(scopes):
    creds = Credentials.from_service_account_file(CREDS_FILE)
    return creds.with_scopes(scopes)

def get_gspread_client(creds):
    return gspread.authorize(creds)

def get_sheet(client, sheet_name):
    return client.open(sheet_name)

def add_user_data_to_sheet(sheet, username, email):
    # Get the first sheet in the workbook
    worksheet = sheet.get_worksheet(0)

    # Check if the headings are present in the first row
    if worksheet.row_values(1) != ["Username", "Email"]:
        # Insert the headings if they are not present
        worksheet.insert_row(["Username", "Email"], 1)

    # Get the values in the first and second columns of the sheet
    usernames = worksheet.col_values(1)
    emails = worksheet.col_values(2)

    while True:
        # Check if the username and email address already exist in the sheet
        if username in usernames:
            print('Error: username already exists')
            username = input("Enter a different username: ")
            continue
        if email in emails:
            print('Error: email address already exists')
            email = input("Enter a different email address: ")
            continue

        # If the username and email are not in the sheet, append the data and exit the loop
        worksheet.append_row([username, email])
        print('User data added successfully')
        break


def main():
    # Get the scoped credentials, client, and sheet
    scoped_creds = get_scoped_credentials(SCOPES)
    client = get_gspread_client(scoped_creds)
    sheet = get_sheet(client, SHEET_NAME)

    for player_num in range(1, 3):
        # Set a flag to indicate if the input is valid
        input_valid = False

        # Run the loop until the input is valid
        while not input_valid:
            # Ask the user for their username and email
            username = input(f'Enter the username for player {player_num}: ')
            email = input(f'Enter the email address for player {player_num}: ')

            # Validate the user input
            if len(username) < 3:
                print('Error: username must be at least 3 characters long')
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                print('Error: email address is not valid')
            else:
                input_valid = True

        # Add the user data to the sheet
        add_user_data_to_sheet(sheet, username, email)

if __name__ == '__main__':
    main()



import re
import gspread
from google.oauth2.service_account import Credentials
import time
from email_validator import validate_email, EmailNotValidError

from datetime import datetime
from typing import NamedTuple

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


class TicTacToeGame:
    def __init__(self, player1, player2, result, duration, date_played):
        self.player1 = player1
        self.player2 = player2
        self.result = result
        self.duration = duration
        self.date_played = date_played

player1 = Player("player1@example.com", "X")
player2 = Player("player2@example.com", "O")
game = TicTacToeGame(player1, player2, "win", 3600, datetime.now())

results = {
    "X": {"wins": 0, "losses": 0, "draws": 0},
    "O": {"wins": 0, "losses": 0, "draws": 0}
}

if game.result == "win":
    results[game.player1.label]["wins"] += 1
    results[game.player2.label]["losses"] += 1
elif game.result == "loss":
    results[game.player1.label]["losses"] += 1
