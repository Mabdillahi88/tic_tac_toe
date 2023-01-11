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


def register_player(username = None, email = None):
    """
    Register a new player using the provided username and email.
    
    Parameters:
        username (str): The desired username.
        email (str): The email address to associate with the username.
    """
    # Validate the email address
    if username and email: 
        try:
            v = validate_email(email)
            email = v["email"]  # Replace the email with the normalized form
        except EmailNotValidError as e:
            print(f"Invalid email address: {e}")
            return False

        # Check if the login details are already in use
        if check_login(username, email):
            print("Username and email are already in use")
            return False

        # Authenticate with Google Sheets API
        creds = Credentials.from_service_account_file(CREDS_FILE, scopes=SCOPES)
        client = gspread.authorize(creds)

        # Open the sheet
        sheet = client.open(SHEET_NAME).sheet1

        # Add the new player to the sheet
        sheet.append_row([username, email])
        print("Registration successful")

        # Prompt player1 to enter login details
        player1_username = input("Player 1, please enter your chosen username: ")
        player1_email = input("Player 1, please enter your email address: ")

        # Prompt player2 to enter login details
        player2_username = input("Player 2, please enter your chosen username: ")
        player2_email = input("Player 2, please enter your email address: ")

        # Register player1
        if register_player(player1_username, player1_email):
            print("Player 1 registered successfully")
        else:
            print("Player 1 registration failed")
            print("try again")
            register_player( username, email)



        if register_player(player2_username, player2_email):
            print("Player 2 registered successfully")
            print("Welcome to Tic Tac Toe!")
            start_tic_tac_toe()
        else:
            print("Player 2 registration failed")
            print("try again")
            register_player( username, email)
    else: 
        return
    


def check_login(username, email):
    """
    Check if the provided username and email are already in use.
    
    Parameters:
        username (str): The username to check.
        email (str): The email address to check.
        
    Returns:
        bool: True if the login details are valid, False otherwise.
    """
    # Validate the email address
    try:
        v = validate_email(email)
        email = v["email"]  # Replace the email with the normalized form
    except EmailNotValidError as e:
        print(f"Invalid email address: {e}")
        return False

    # Authenticate with Google Sheets API
    creds = Credentials.from_service_account_file(CREDS_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)

    # Open the sheet
    sheet = client.open(SHEET_NAME).sheet1

    # Search for the username and email in the sheet
    cell = sheet.find(username)
    if cell is None:
        return False
    row = cell.row
    if sheet.cell(row, 2).value != email:
        return False

    return True

    # Prompt player1 to enter login details
player1_username = input("Player 1, please enter your username: ")
player1_email = input("Player 1, please enter your email address: ")

# Prompt player2 to enter login details
player2_username = input("Player 2, please enter your username: ")
player2_email = input("Player 2, please enter your email address: ")

# Check player1 login details
if check_login(player1_username, player1_email):
    print("Player 1 login successful")
else:
    print("Player 1 login failed")
    print("Please register")
    register_player(username=None, email=None)

# Check player2 login details
if check_login(player2_username, player2_email):
    print("Player 2 login successful")
    print("Welcome to Tic Tac Toe!")
    start_tic_tac_toe()
else:
    print("Player 2 login failed")
    print("Please register")
    register_player(username=None, email=None)


    
def register_player(username, email):
    """
    Register a new player using the provided username and email.
    
    Parameters:
        username (str): The desired username.
        email (str): The email address to associate with the username.
    """
    # Validate the email address
    try:
        v = validate_email(email)
        email = v["email"]  # Replace the email with the normalized form
    except EmailNotValidError as e:
        print(f"Invalid email address: {e}")
        return False

 