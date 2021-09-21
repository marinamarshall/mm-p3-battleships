# from random import randint
import random

board = []
miss = []

for x in range(0, 4):
    board.append(["-"] * 4)


def print_battleships_board(board):
    """
    Display the game board to the user
    """
    for place in board:
        print(" ".join(place))


def random_row(board):
    """
    Set the ship row at random
    """
    return random.randint(0, 3)


def random_col(board):
    """
    Set the ship column at random
    """
    return random.randint(0, 3)    

# Define global variables
ship_row = random_row(board)
ship_col = random_col(board)

def main():
    # Greeting the user.
    print("Welcome to Battleships!\n")
    print("You get 10 bullets to play against the computer")
    print_battleships_board(board)
    random_row(board)
    random_col(board)
    
    try:
        for turn in range(5):
        guess_row = int(input("Guess a Row: (between 0 and 3)\n"))
        guess_col = int(input("Guess a Column: (between 0 and 3) \n"))
    except ValueError:
        print("Invalid user input, try again")      


main()