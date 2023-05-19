import gspread
from google.oauth2.service_account import Credentials
from email_validator import validate_email, EmailNotValidError


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS_FILE = 'creds.json'
SHEET_NAME = 'Tic_tac_toe'


def get_scoped_credentials(scopes):
    """
    This function returns the credentials with the provided scopes.
    """
    creds = Credentials.from_service_account_file(CREDS_FILE)
    return creds.with_scopes(scopes)


def get_gspread_client(creds):
    """
    This function authenticates and returns a Google Sheets client.
    """
    return gspread.authorize(creds)


def get_sheet(client, sheet_name):
    """
    This function returns the Google Sheets document by its name.
    """
    return client.open(sheet_name)


def add_user_data_to_sheet(sheet, player_num, username, email):
    """
    This function adds the user data to the Google Sheets document.
    """
    worksheet = sheet.get_worksheet(0)
    if worksheet.row_values(1) != ["Username", "Email"]:
        worksheet.insert_row(["Username", "Email"], 1)
    usernames = worksheet.col_values(1)
    emails = worksheet.col_values(2)

    while True:
        try:
            v = validate_email(email)
            email = v.email
        except EmailNotValidError as e:
            print(f"Invalid email address: {str(e)}")
            email = input("Enter a valid email address: ")
            continue

        if username in usernames:
            print(f'Error: {username} already exists')
            username = input("Enter a different username: ")
            continue
        if email in emails:
            print(f'Error: {email} already exists')
            email = input("Enter a different email address: ")
            continue

        worksheet.append_row([username, email])
        print(f'Player {player_num} data added successfully')
        break


def login_or_register(sheet, player_num):
    """
    This function handles the user login or registration.
    """
    while True:
        print(f"Player {player_num}, please choose an option:")
        print("1) Login")
        print("2) Register")
        selection = input("Enter your choice: ")

        if selection == "1":
            username = input("Enter your username: ")
            email = input("Enter your email address: ")
            worksheet = sheet.get_worksheet(0)
            usernames = worksheet.col_values(1)
            emails = worksheet.col_values(2)
            if username in usernames and email in emails:
                print(f"Welcome back, {username}!")
                return username
            else:
                print("Invalid username or email. "
                      "Please try again or register.")
        elif selection == "2":
            username = input("Enter a new username: ")
            email = input("Enter a new email address: ")
            try:
                add_user_data_to_sheet(sheet, player_num, username, email)
                print("Registration successful.")
                return username
            except Exception as e:
                print(f"An error occurred during registration: {e}")
                print("Please try again.")
        else:
            print("Invalid option selected. Please choose either 1 or 2.")


"""
The program starts here.

First, it gets credentials with the defined SCOPES. Then, it gets the
Google Sheets client with these credentials. It then accesses the Google
Sheets document by its name.

Two players log in or register, and their usernames are printed out.
"""
credentials = get_scoped_credentials(SCOPES)
client = get_gspread_client(credentials)
sheet = get_sheet(client, SHEET_NAME)
player1_username = login_or_register(sheet, 1)
player2_username = login_or_register(sheet, 2)

print(f"Player 1: {player1_username}")
print(f"Player 2: {player2_username}")
