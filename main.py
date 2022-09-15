import random

def user_turn():
    user_choice = input("\nPlease enter your spot choice: ")

    user_choice = int(user_choice)
    board[user_choice] = 'X'
    open_spaces.remove(user_choice)

    try:
        open_spaces.remove(user_choice)
    except ValueError:
        print("You have selected an invalid space. Please try again. ")

def printBoard():

    print(f"{board[1]} | {board[2]} | {board[3]}")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print(f"{board[7]} | {board[8]} | {board[9]}")

def comp_turn():
    comp_choice = random.choice(open_spaces)
    comp_choice = int(comp_choice)
    if board[comp_choice] == 'X':
        comp_choice = random.choice(open_spaces)
        board[comp_choice] = 'O'    
    else:
        board[comp_choice] = 'O'   
    
    try:
        open_spaces.remove(comp_choice)
    except ValueError:
        comp_choice = random.choice(open_spaces)

def check_win():
    global game_on

    if board[1] == 'X' and board[2] == 'X' and board[3] == 'X':
        print("You win!")
        game_on = False

    elif board[4] == 'X' and board[5] == 'X' and board[6] == 'X':
        print("You win!")
        game_on = False

    elif board[7] == 'X' and board[8] == 'X' and board[9] == 'X':
        print("You win!")
        game_on = False

    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        print("You win!")
        game_on = False

    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        print("You win!")
        game_on = False

    elif board[3] == 'X' and board[6] == 'X' and board[9] == 'X':
        print("You win!")
        game_on = False

    elif board[1] == 'X' and board[5] == 'X' and board[9] == 'X':
        print("You win!")
        game_on = False

    if board[3] == 'X' and board[5] == 'X' and board[7] == 'X':
        print("You win!")
        game_on = False

    if board[1] == 'O' and board[2] == 'O' and board[3] == 'O':
        print("You lose")
        game_on = False

    elif board[4] == 'O' and board[5] == 'O' and board[6] == 'O':
        print("You lose")
        game_on = False

    elif board[7] == 'O' and board[8] == 'O' and board[9] == 'O':
        print("You lose")
        game_on = False

    elif board[1] == 'O' and board[5] == 'O' and board[9] == 'O':
        print("You lose")
        game_on = False

    elif board[3] == 'O' and board[5] == 'O' and board[7] == 'O':
        print("You lose")
        game_on = False

    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        print("You lose")
        game_on = False

    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        print("You lose")
        game_on = False

    elif board[3] == 'O' and board[6] == 'O' and board[9] == 'O':
        print("You lose")
        game_on = False

board = {num:'_' for num in range(1, 10)}
game_on = True
open_spaces = [x for x in range(1, 9)]

print("Moving from top left to bottom right, spaces are numbered 1 - 9.\n")
printBoard()

while game_on:
    user_turn()
    check_win()
    comp_turn()
    printBoard()
    check_win()
    

    
