import random

board = {num:'_' for num in range(1, 10)}

def user_turn():
    user_choice = input("Moving from top left to bottom right, spaces are numbered 1 - 9. Please enter the space you'd like to mark for your turn.\n")

    user_choice = int(user_choice)
    board[user_choice] = 'X'


def printBoard():

    print(f"{board[1]} | {board[2]} | {board[3]}")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print(f"{board[7]} | {board[8]} | {board[9]}")

def comp_turn():
    comp_choice = random.choice(range(1, 10))
    if board[comp_choice] != 'X':
        board[comp_choice] = 'O'
    else:
        comp_choice = random.choice(range(1, 10))

game_on = True

while game_on:
    printBoard()
    user_turn()
    comp_turn()