from globals import GlobalInfo


def is_game_over():
    if GlobalInfo.board[1] == 'X' and GlobalInfo.board[2] == 'X' and GlobalInfo.board[3] == 'X':
        print("You win!")
        GlobalInfo.gameOn = False

    elif GlobalInfo.board[4] == 'X' and GlobalInfo.board[5] == 'X' and GlobalInfo.board[6] == 'X':
        print("You win!")
        GlobalInfo.gameOn = False

    elif GlobalInfo.board[7] == 'X' and GlobalInfo.board[8] == 'X' and GlobalInfo.board[9] == 'X':
        print("You win!")
        GlobalInfo.gameOn = False

    elif GlobalInfo.board[1] == 'X' and GlobalInfo.board[4] == 'X' and GlobalInfo.board[7] == 'X':
        print("You win!")
        GlobalInfo.gameOn = False

    elif GlobalInfo.board[2] == 'X' and GlobalInfo.board[5] == 'X' and GlobalInfo.board[8] == 'X':
        print("You win!")
        GlobalInfo.gameOn = False

    elif GlobalInfo.board[3] == 'X' and GlobalInfo.board[6] == 'X' and GlobalInfo.board[9] == 'X':
        print("You win!")
        GlobalInfo.gameOn = False

    elif GlobalInfo.board[1] == 'X' and GlobalInfo.board[5] == 'X' and GlobalInfo.board[9] == 'X':
        print("You win!")
        GlobalInfo.gameOn = False

    if GlobalInfo.board[3] == 'X' and GlobalInfo.board[5] == 'X' and GlobalInfo.board[7] == 'X':
        print("You win!")
        GlobalInfo.gameOn = False

    if GlobalInfo.board[1] == 'O' and GlobalInfo.board[2] == 'O' and GlobalInfo.board[3] == 'O':
        print("You lose")
        GlobalInfo.gameOn = False

    elif GlobalInfo.board[4] == 'O' and GlobalInfo.board[5] == 'O' and GlobalInfo.board[6] == 'O':
        print("You lose")
        GlobalInfo.gameOn = False

    elif GlobalInfo.board[7] == 'O' and GlobalInfo.board[8] == 'O' and GlobalInfo.board[9] == 'O':
        print("You lose")
        GlobalInfo.gameOn = False

    elif GlobalInfo.board[1] == 'O' and GlobalInfo.board[5] == 'O' and GlobalInfo.board[9] == 'O':
        print("You lose")
        GlobalInfo.gameOn = False

    elif GlobalInfo.board[3] == 'O' and GlobalInfo.board[5] == 'O' and GlobalInfo.board[7] == 'O':
        print("You lose")
        GlobalInfo.gameOn = False

    elif GlobalInfo.board[1] == 'O' and GlobalInfo.board[4] == 'O' and GlobalInfo.board[7] == 'O':
        print("You lose")
        GlobalInfo.gameOn = False

    elif GlobalInfo.board[2] == 'O' and GlobalInfo.board[5] == 'O' and GlobalInfo.board[8] == 'O':
        print("You lose")
        GlobalInfo.gameOn = False

    elif GlobalInfo.board[3] == 'O' and GlobalInfo.board[6] == 'O' and GlobalInfo.board[9] == 'O':
        print("You lose")
        GlobalInfo.gameOn = False

    if not GlobalInfo.gameOn:
        if len(GlobalInfo.openSpaces) == 0:
            print("It's a draw")
            GlobalInfo.gameOn = False
