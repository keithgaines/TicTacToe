from globals import global_info
from turns import turn
from check_win import check_win

def printBoard():

    print(f"{global_info.board[1]} | {global_info.board[2]} | {global_info.board[3]}")
    print(f"{global_info.board[4]} | {global_info.board[5]} | {global_info.board[6]}")
    print(f"{global_info.board[7]} | {global_info.board[8]} | {global_info.board[9]}")


global_info.gameOn = True


print("Moving from top left to bottom right, spaces are numbered 1 - 9.\n")
printBoard()

while global_info.gameOn:
    turn.user()
    turn.comp()
    printBoard()
    check_win.isGameOver()
    

    
