from ast import Global
import random
from globals import GlobalInfo
import check_win

def playgame():
    
    count = 0

    while GlobalInfo.gameOn:
        turn = 'X'
        space = input("Please select a space: ")
        space = int(space)
       
        while GlobalInfo.board[space] == 'O':
            print("Invalid selection.")
            space = input("Please select a space: ")
        
        GlobalInfo.board[space] = turn  
        GlobalInfo.printboard()

        check_win.is_game_over()

        turn = 'O'
        comp_space = random.randint(1, 9)

        while GlobalInfo.board[comp_space] != '_':
            comp_space = random.randint(1, 9)
        if GlobalInfo.board[comp_space] == '_':
            GlobalInfo.board[comp_space] = turn
        GlobalInfo.printboard()
        
        if turn == 'X':
            turn = 'O'
            count += 1

        else:
            turn = 'X'

        check_win.is_game_over()
        if GlobalInfo.gameOn == False:
            break
        