# Example 2-12. A list with three lists of length 3 can represent a tic-tac-toe board

board = [['_']*3 for i in range(3)]
board[1][2] = 'X'

print(board)


board = []
for i in range(3):
    row = ['_'] * 3 #
    board.append(row)