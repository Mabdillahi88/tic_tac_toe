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


def login(username, email):
    # Get the values in the first and second columns of the sheet
    usernames = worksheet.col_values(1)
    emails = worksheet.col_values(2)

    # Check if the username and email are registered
    if username in usernames and email in emails:
        # Find the row where the login and email appear
        cell = worksheet.find(username)
        row = cell.row
        # Retrieve the name and score from the row
        name = worksheet.row_values(row)[0]
        score = int(worksheet.row_values(row)[2])
        print(f"\nWelcome back, {name}!\n")
    else:
        print("Username and email not registered. Please try again.")







def add_user_data_to_sheet(sheet, username, email):
    # Get the first sheet in the workbook
    worksheet = sheet.get_worksheet(0)

    # Check if the headings are present in the first row
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
        if not username:
            print("Error: username cannot be empty.")
            username = input("Enter a valid username: ")
            continue
        if not email:
            print("Error: email cannot be empty.")
            email = input("Enter a valid email: ")
            continue
        try:
            validated_email = validate_email(email)
            email = validated_email.email
        except EmailNotValidError as e:
            print("Error: invalid email format.")
            email = input("Enter a valid email: ")
            continue
        if username in usernames:
            print('Error: username already exists')
            username = input("Enter a different username: ")
            continue
        if email in emails:
            print('Error: email address already exists')
            email = input("Enter a different email address: ")
            continue
        # If the username and email are not in the sheet and are in a valid format, append the data and exit the loop
        worksheet.append_row([username, email])
        print('User data added successfully')
        break

