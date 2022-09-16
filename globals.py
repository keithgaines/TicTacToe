class GlobalInfo:
    board = {num: '_' for num in range(1, 10)}
    openSpaces = [x for x in range(1, 10)]
    gameOn = True
    
    def printboard():
        print(f"\n{GlobalInfo.board[1]} | {GlobalInfo.board[2]} | {GlobalInfo.board[3]}")
        print(f"{GlobalInfo.board[4]} | {GlobalInfo.board[5]} | {GlobalInfo.board[6]}")
        print(f"{GlobalInfo.board[7]} | {GlobalInfo.board[8]} | {GlobalInfo.board[9]}")
