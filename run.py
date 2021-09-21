# from random import randint
import random

board = []

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


def main():
    # Greeting the user.
    print("Welcome to Battleships!\n")
    print("You get 10 bullets to play against the computer")
    print_battleships_board(board)
    random_row(board)
    random_col(board)
