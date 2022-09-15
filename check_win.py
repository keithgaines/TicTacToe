from globals import global_info

class check_win:
    def isGameOver():

        if global_info.board[1] == 'X' and global_info.board[2] == 'X' and global_info.board[3] == 'X':
            print("You win!")
            global_info.gameOn = False

        elif global_info.board[4] == 'X' and global_info.board[5] == 'X' and global_info.board[6] == 'X':
            print("You win!")
            global_info.gameOn = False

        elif global_info.board[7] == 'X' and global_info.board[8] == 'X' and global_info.board[9] == 'X':
            print("You win!")
            global_info.gameOn = False

        elif global_info.board[1] == 'X' and global_info.board[4] == 'X' and global_info.board[7] == 'X':
            print("You win!")
            global_info.gameOn = False

        elif global_info.board[2] == 'X' and global_info.board[5] == 'X' and global_info.board[8] == 'X':
            print("You win!")
            global_info.gameOn = False

        elif global_info.board[3] == 'X' and global_info.board[6] == 'X' and global_info.board[9] == 'X':
            print("You win!")
            global_info.gameOn = False

        elif global_info.board[1] == 'X' and global_info.board[5] == 'X' and global_info.board[9] == 'X':
            print("You win!")
            global_info.gameOn = False

        if global_info.board[3] == 'X' and global_info.board[5] == 'X' and global_info.board[7] == 'X':
            print("You win!")
            global_info.gameOn = False

        if global_info.board[1] == 'O' and global_info.board[2] == 'O' and global_info.board[3] == 'O':
            print("You lose")
            global_info.gameOn = False

        elif global_info.board[4] == 'O' and global_info.board[5] == 'O' and global_info.board[6] == 'O':
            print("You lose")
            global_info.gameOn = False

        elif global_info.board[7] == 'O' and global_info.board[8] == 'O' and global_info.board[9] == 'O':
            print("You lose")
            global_info.gameOn = False

        elif global_info.board[1] == 'O' and global_info.board[5] == 'O' and global_info.board[9] == 'O':
            print("You lose")
            global_info.gameOn = False

        elif global_info.board[3] == 'O' and global_info.board[5] == 'O' and global_info.board[7] == 'O':
            print("You lose")
            global_info.gameOn = False

        elif global_info.board[1] == 'O' and global_info.board[4] == 'O' and global_info.board[7] == 'O':
            print("You lose")
            global_info.gameOn = False

        elif global_info.board[2] == 'O' and global_info.board[5] == 'O' and global_info.board[8] == 'O':
            print("You lose")
            global_info.gameOn = False

        elif global_info.board[3] == 'O' and global_info.board[6] == 'O' and global_info.board[9] == 'O':
            print("You lose")
            global_info.gameOn = False