import gspread
from google.oauth2.service_account import Credentials
import sys
import time
from time import sleep
import os
import random
from validation2 import get_scoped_credentials, get_gspread_client, get_sheet, login_or_register


# OAuth 2.0 scopes required to access Google Sheets and Drive
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

def lets_play_noughts_and_crosses():
    player1_username, player2_username = validation2.get_players()

def cls():
    """
    Clear the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")

def separate_line():
    """
    Print a line separator.
    """
    print("\n" + "-"*30 + "\n")


