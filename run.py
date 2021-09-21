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

print_battleships_board(board)
