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
