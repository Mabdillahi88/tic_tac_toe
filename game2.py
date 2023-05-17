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

def add_user_data_to_sheet(sheet, player_num, username, email):
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
            print(f'Error: Player {player_num} username already exists')
            username = input(f"Enter a different username for Player {player_num}: ")
            continue
        if email in emails:
            print(f'Error: Player {player_num} email address already exists')
            email = input(f"Enter a different email address for Player {player_num}: ")
            continue

        # If the username and email are not in the sheet, append the data and exit the loop
        worksheet.append_row([username, email])
        print('User data added successfully')
        break



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

def add_user_data_to_sheet(sheet, player_num, username, email):
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
        try:
            # Validate the email address
            v = validate_email(email)
            email = v.email  # Replace the email with the normalized form
        except EmailNotValidError as e:
            print(f"Invalid email address: {str(e)}")
            email = input("Enter a valid email address: ")
            continue

        # Check if the username and email address already exist in the sheet
        if username in usernames:
            print(f'Error: {username} already exists')
            username = input("Enter a different username: ")
            continue
        if email in emails:
            print(f'Error: {email} already exists')
            email = input("Enter a different email address: ")
            continue

        # If the username and email are not in the sheet, append the data and exit the loop
        worksheet.append_row([username, email])
        print(f'Player {player_num} data added successfully')
        break

# Usage example
player1_username = input("Player 1, please enter your username: ")
player1_email = input("Player 1, please enter your email address: ")

player2_username = input("Player 2, please enter your username: ")
player2_email = input("Player 2, please enter your email address: ")

# Get the scoped credentials
credentials = get_scoped_credentials(SCOPES)

# Get the gspread client
client = get_gspread_client(credentials)

# Get the sheet
sheet = get_sheet(client, SHEET_NAME)

# Add user data to the sheet
add_user_data_to_sheet(sheet, 1, player1_username, player1_email)
add_user_data_to_sheet(sheet, 2, player2_username, player2_email)


import gspread
from google.oauth2.service_account import Credentials
from email_validator import validate_email, EmailNotValidError

# OAuth 2.0 scopes required to access Google Sheets and Drive
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# File name of the credentials JSON file
CREDS_FILE = 'creds.json'

# Name of the Google Sheet to be accessed
SHEET_NAME = 'Tic_tac_toe'

def get_scoped_credentials():
    # Load credentials from the JSON file and add the required scopes
    creds = Credentials.from_service_account_file(CREDS_FILE)
    return creds.with_scopes(SCOPES)

def get_gspread_client():
    # Authorize the client using the scoped credentials
    credentials = get_scoped_credentials()
    return gspread.authorize(credentials)

def get_sheet(sheet_name):
    # Get the Google Sheet with the given name
    client = get_gspread_client()
    return client.open(sheet_name)

def add_user_data_to_sheet(sheet, player_num, username, email):
    # Get the first worksheet in the workbook
    worksheet = sheet.get_worksheet(0)

    # Get the existing usernames and emails in the sheet
    usernames = worksheet.col_values(1)
    emails = worksheet.col_values(2)

    while True:
        try:
            # Validate the email address and normalize it
            email = validate_email(email).email
        except EmailNotValidError as e:
            print(f"Invalid email address: {str(e)}")
            email = input("Enter a valid email address: ")
            continue

        # Check for duplicate usernames and emails
        if username in usernames:
            print(f'Error: {username} already exists')
            username = input("Enter a different username: ")
            continue
        if email in emails:
            print(f'Error: {email} already exists')
            email = input("Enter a different email address: ")
            continue

        # If no duplicates found, append the data to the sheet
        worksheet.append_row([username, email])
        print(f'Player {player_num} data added successfully')
        break

def prompt_player_data(player_num):
    # Prompt the player to enter their username and email address
    username = input(f"Player {player_num}, please enter your username: ")
    email = input(f"Player {player_num}, please enter your email address: ")
    return username, email

def main():
    # Get the Google Sheet
    sheet = get_sheet(SHEET_NAME)

    # Prompt player 1 for their data
    player1_username, player1_email = prompt_player_data(1)

    # Prompt player 2 for their data
    player2_username, player2_email = prompt_player_data(2)

    # Add player data to the sheet
    add_user_data_to_sheet(sheet, 1, player1_username, player1_email)
    add_user_data_to_sheet(sheet, 2, player2_username, player2_email)

if __name__ == "__main__":
    # Execute the main function when the script is run directly
    main()
