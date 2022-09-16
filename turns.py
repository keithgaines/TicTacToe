from ast import Global
import random
from globals import GlobalInfo
import check_win

def playgame():
    turn = 'X'
    count = 0

    while GlobalInfo.gameOn:
        space = input("Please select a space: ")
        space = int(space)
        GlobalInfo.board[space] = turn
        try:
            GlobalInfo.openSpaces.remove(space)
        except ValueError:
            print("You have selected an invalid space. Please try again. ")    
        GlobalInfo.printboard()
        if turn == 'X':
            turn = 'O'
            count += 1

        else:
            turn = 'X'

        check_win.is_game_over()
        