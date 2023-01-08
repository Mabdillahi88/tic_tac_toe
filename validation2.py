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

def check_login(username, email):
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

player1_username = input("Player 1, please enter your username: ")
player1_email = input("Player 1, please enter your email address: ")

player2_username = input("Player 2, please enter your username: ")
player2_email = input("Player 2, please enter your email address: ")

if check_login(player1_username, player1_email):
    print("Player 1 login successful")
else:
    print("Player 1 login failed")

if check_login(player2_username, player2_email):
    print("Player 2 login successful")
else:
    print("Player 2 login failed")
