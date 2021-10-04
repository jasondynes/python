# Milestone Project 1: Walkthrough Steps Workbook
# Author: Jason Dynes
# Date: 8th October 2019

# To take input from a user:
# player1 = input("Please pick a marker 'X' or 'O'")
# Note that input() takes in a string. If you need an integer value, use
# position = int(input('Please enter a number'))

# To clear the screen between moves:
# from IPython.display import clear_output
# clear_output()
# Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:
# print('\n'*100)
# This scrolls the previous board up out of view. Now on to the program!

# from IPython.display import clear_output
# print('\n' * 100)

import random


# Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds
# with a number on a number pad, so you get a 3 by 3 board representation.
def display_board(board):
    len(board)
    # print("   |   |")
    print(f" {board[7]} | {board[8]} | {board[9]}")
    print("------------")
    # print("   |   |")
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print("------------")
    # print("   |   |")
    print(f" {board[1]} | {board[2]} | {board[3]}")


# TEST Step 1: run your function on a test version of the board list, and make adjustments as necessary
# test_board = ['#','X','O','X','O','X','O','X','O','X']

# test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# display_board(test_board)


# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using
# while loops to continually ask until you get a correct answer.
def player_input(player):
    global position, marker
    valid = 0
    while valid == 0:
        print(f"Player {player}: Could you enter your selection please?")
        position = int(input())
        if position < 1 or position > 9:
            print("INVALID: Choose a number between 1 and 9")
            pass
        elif test_board[position] == ' ':
            valid = 1
            if player == 1:
                marker = 'X'
            else:
                marker = 'O'
        else:
            print("INVALID: Position is already occupied by a X or O")
    return position, marker


# TEST Step 2: run the function to make sure it returns the desired output
# board_position = 0
# player = 1
# player = player_input(player)


# display_board(test_board)


# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number
# 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    assert isinstance(marker, str)
    board[position] = marker


# TEST Step 3: run the place marker function using test parameters and display the modified board
# place_marker(test_board, '$', 8)
# display_board(test_board)


# Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. *
def win_check(board, mark):
    if board[7] == mark and board[5] == mark and board[3] == mark or \
            board[1] == mark and board[5] == mark and board[9] == mark or \
            board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[1] == mark and board[2] == mark and board[3] == mark or \
            board[7] == mark and board[4] == mark and board[1] == mark or \
            board[8] == mark and board[5] == mark and board[2] == mark or \
            board[9] == mark and board[6] == mark and board[3] == mark:
        return True
    else:
        return False


# TEST Step 4: run the win_check function against our test_board - it should return True
# print(win_check(test_board, 'X'))

# Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to
# lookup random.randint() Return a string of which player went first.

def choose_first():
    playerstart = random.randint(1, 2)
    assert isinstance(playerstart, int)
    return playerstart


# playerstart = choose_first()
# print(playerstart)

# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    spccount = 0
    for x in range(1, 10):
        # print(x)
        if board[x] == ' ':
            spccount = spccount + 1
        # print("TEST")
    if spccount > 0:
        return False
    else:
        return True


# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from
# step 6 to check if it's a free position. If it is, then return the position for later use.

def player_choice(board):
    valid = 0
    while valid == 0:
        print(f("Player {player}: Could you enter your selection please?"))
        position = int(input())
        if position < 1 or position > 9:
            print("INVALID: Choose a number between 1 and 9")
            pass
        elif not space_check(board, position):
            print("INVALID: Position is already occupied by a X or O")
        else:
            return position


# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want
# to play again.

def replay():
    print("Do you want to play again?")
    resp = input()
    if resp.lower() == "y":
        return True
    else:
        return False


# Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!
# print('Welcome to Tic Tac Toe!')

# Main call routine for Tic Tac Toe Game
end_game = False
global playerstart
board_position = 0
test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

while end_game is not True:
    # Set the game up here

    # Display initial blank board
    display_board(test_board)
    game_on = True

    # Choose which player goes first (Ref: Step 5)
    playerstart = choose_first()
    print(f"Player {playerstart} goes first")
    # set player to start first
    player = playerstart

    while game_on:
        # returns position, marker for a stated player. If Player 1 is X or 2 is O
        playermove = player_input(player)

        # Step 3 function
        place_marker(test_board, marker, position)

        # refresh game board displayed
        print('\n' * 100)
        display_board(test_board)

        # check if player wins (Step 4 function)
        mark = marker
        if win_check(test_board, mark):
            print(f"Player {player} has won !!!")
            game_on = False
        # check if board full
        elif full_board_check(test_board):
            print("Board is Full so game is a draw !!!")
            game_on = False

        # change player
        print(f"player {player} before")
        if player == 1:
            player = 2
        else:
            player = 1
        print(f"player {player} after")
    # if not replay():
    if replay() is False:
        end_game = True
        print("Game is ending.....")
    else:
        test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
