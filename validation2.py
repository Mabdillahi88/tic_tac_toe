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
