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
