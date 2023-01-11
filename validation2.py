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

