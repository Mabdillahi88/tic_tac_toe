"""
A tic-tac-toe game built with Python and Tkinter.
"""

import tkinter as tk
import os
import time
from itertools import cycle
from tkinter import font
from typing import NamedTuple

class Player(NamedTuple):
    label: str
    color: str

class Move(NamedTuple):
    row: int
    col: int
    label: str = ""

BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="green"),
)

def display_logo():
    """
    Display game name and rules
    """
    print("Welcome to Tic Tac Toe!")
    print(" ")
    print("The goal of the game is to get three of your symbols in a row (horizontally, vertically, or diagonally) before your opponent does.")
    print("You will be asked to enter the row and column where you want to place your symbol (X or O) on the board.")
    print(" ")
    time.sleep(1)

def clear_console():
    """
    Clear the console
    """
    os.system("cls" if os.name == "nt" else "clear")

def display_separator():
    """
    Print '-' lines to separate messages
    """
    print(" ")
    print("- "*30)
    print(" ")
def main_menu() -> str:
    """
    The program will first show two possible options of the game
    User can select to view game rules or start game
    """
    display_logo()
    time.sleep(1)
    print("What would you like to do?")
    start_options = "1) View game rules\n2) Play game\n"
    start_option_selected = input(start_options)
    display_separator()

    # Validate if answer is either 1 or 2
    while start_option_selected not in ("1", "2"):
        print("Please choose between one of the two options:")
        start_option_selected = input(start_options)
        display_separator()

    if start_option_selected == "1":
        clear_console()
        display_logo()
        game_rules()

    elif start_option_selected == "2":
        start_game()

    return start_option_selected
main_menu()


import os
import time

def clear_screen():
  """
  Clear the console screen
  """
  os.system("cls" if os.name == "nt" else "clear")

def display_game_title():
  """
  Display the game title and rules
  """
  clear_screen()
  print("Welcome to Tic Tac Toe!")
  print(" ")
  print("The goal of the game is to get three of your symbols in a row (horizontally, vertically, or diagonally) before your opponent does.")
  print("You will be asked to enter the row and column where you want to place your symbol (X or O) on the board.")
  print(" ")
  time.sleep(1)

display_game_title()


import random
import sys
import time
import os
import tkinter as tk
import copy

import time
from colors import Color as Col
import os
import time


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


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def separate_line():
    print("\n" + "-"*30 + "\n")
    
def main_menu() -> str:
    """
    Display a welcome message and the rules of Tic-Tac-Toe
    Prompt the user to choose between logging in or registering
    """
    print("Welcome to Tic-Tac-Toe!\n")
    print("In this game, you and your opponent will take turns placing X or O on a 3x3 grid. The first player to get 3 of their symbols in a row (horizontally, vertically, or diagonally) wins the game.\n")
    login_options = "1) Log in\n2) Register\n"
    login_option_selected = input("Please choose an option:\n" + login_options)
    separate_line()

    # Validate if answer is either 1 or 2
    while login_option_selected not in ("1", "2"):
        print("Please choose between one of the two options:")
        login_option_selected = input(login_options)
        separate_line()

def login_menu() -> Tuple[str, str]:
    """
    Prompt the user to enter their username and email address
    Return the username and email as a tuple
    """
    username = input("Please enter your username: ")
    email = input("Please enter your email address: ")
    return username, email


def main_menu() -> str:
    """
    Display a welcome message and the rules of Tic-Tac-Toe
    Prompt the user to choose between logging in or registering
    """
    print("Welcome to Tic-Tac-Toe!\n")
    print("In this game, you and your opponent will take turns placing X or O on a 3x3 grid. The first player to get 3 of their symbols in a row (horizontally, vertically, or diagonally) wins the game.\n")
    login_options = "1) Log in\n2) Register\n"
    login_option_selected = input("Please choose an option:\n" + login_options)
    separate_line()

    # Validate if answer is either 1 or 2
    while login_option_selected not in ("1", "2"):
        print("Please choose between one of the two options:")
        login_option_selected = input(login_options)
        separate_line()

    # If the user selected "Log in", prompt them for their username and email
    if login_option_selected == "1":
        username, email = login_menu()
    # If the user selected "Register", create a new account for them
    else:
        username, email = login_menu()
        create_account(username, email)