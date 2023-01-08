

def logo():
    """
    Display the game logo.
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
    """
    Clear the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def separate_line():
    """
    Print a line separator.
    """
    print("\n" + "-"*30 + "\n")

def main_menu():
    """
    Display the main menu and prompt the user to choose between logging in or registering.
    """
    print("Welcome to Tic-Tac-Toe!\n")
  
    options = "1) Log in\n2) Register\n"
    selection = input("Please choose an option:\n" + options)
    separate_line()

    # Validate the user's input to make sure it is either 1 or 2
    while selection not in ("1", "2"):
        print("Please choose between one of the two options:")
        selection = input(options)
        separate_line()
    
    # If the user chooses to log in, call the login_users function
    if selection == "1":
        get_login_and_email()
  
    # If the user chooses to register, call the register_players function
    elif selection == "2":
        register_new_user()

    return selection



def lets_play_tic_tac_toe():
  print("Welcome to Tic Tac Toe!")
  print("The rules of the game are as follows:")
  print("1. The game is played on a 3x3 grid.")
  print("2. Players take turns placing their respective symbols (X or O) on the grid.")
  print("3. The first player to get 3 of their symbols in a row (horizontally, vertically, or diagonally) wins the game.")
  print("4. If all of the spaces on the grid are filled and no player has won, the game is a draw.")
  print("Let's begin!")
  separate_line()



class Player(NamedTuple):
    """Represents a player in the game."""
    label: str
    color: str

class Move(NamedTuple):
    """Represents a move made by a player."""
    row: int
    col: int
    label: str = ""

BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),  # Player 1
    Player(label="O", color="green"), # Player 2
)

# Initialize the game board with empty spaces
board = [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_board():
    """Print the current state of the game board."""
    for row in board:
        print(" ".join(row))

print_board()


