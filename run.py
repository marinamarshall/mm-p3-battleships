import random

board = []
miss = []

# Define what the game board will look like
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
print(ship_row)

ship_col = random_col(board)
print(ship_col)


def user_answer():
    """
    Ask user for input for row and column value.
    Validate this information provided by using a try/
    except statement
    Update the turn count and display to the user
    """
    # Initialize turns to be at zero
    turns = 0
    for turn in range(10):
        guess_row = int(input("Guess a Row: (between 0 and 3)\n"))
        guess_col = int(input("Guess a Column: (between 0 and 3) \n"))

        if (guess_row == ship_row and guess_col == ship_col):
            board[guess_row][guess_col] = "X"
            print("Congratulations! You sunk the battleship, You Win!")
            print_battleships_board(board)
            turns = turns + 1
            print("you are on guess " + str(turns) + " of 10")
            break
        elif (guess_row != ship_row and guess_col != ship_col):
            board[guess_row][guess_col] = "O"
            miss.append([guess_row, guess_col])
            print("Ansewrs you have guessed:" + str(miss))
            print("You Missed! Try Again")
            print_battleships_board(board)
            turns = turns + 1
            print("you are on guess " + str(turns) + " of 10")
        else:
            if (guess_row < 0 or guess_row > 3)  or (guess_col < 0 or guess_col > 3):
                print ("Oops, you missed! Try again")
            elif guess_row and guess_col in miss:
                raise ValueError("Value already guessed, please guess again")
            else:
                print(f"Invalid data: {e}, please try again.\n")         


def main():
    # Greeting the user.
    print("Welcome to Battleships!\n")
    print("You get 10 bullets to play against the computer")
    print_battleships_board(board)
    user_answer()


main()