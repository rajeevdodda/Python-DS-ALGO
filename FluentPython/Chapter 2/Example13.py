# Example 2-13. A list with three references to the same list is useless

weird_board = [['_'] * 3] * 3
weird_board[1][2] = 'O'
print(weird_board)

row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)