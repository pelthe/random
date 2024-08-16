board = []
 
for i in range(8):
    row = ["" for i in range(8)]
    board.append(row)

board[1][0] = "PAWN"
board[1][1] = "PAWN"
board[1][2] = "PAWN"
board[1][3] = "PAWN"
board[1][4] = "PAWN"
board[1][5] = "PAWN"
board[1][6] = "PAWN"
board[1][7] = "PAWN"
board[6][0] = "PAWN"
board[6][1] = "PAWN"
board[6][2] = "PAWN"
board[6][3] = "PAWN"
board[6][4] = "PAWN"
board[6][5] = "PAWN"
board[6][6] = "PAWN"
board[6][7] = "PAWN"
board[0][0] = "ROOK"
board[0][7] = "ROOK"
board[7][0] = "ROOK"
board[7][7] = "ROOK"
board[0][1] = "KNIGHT"
board[0][6] = "KNIGHT"
board[7][1] = "KNIGHT"
board[7][6] = "KNIGHT"

print(board)
