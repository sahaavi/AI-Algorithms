rows, cols = (8, 8)
board = [['x' for i in range(cols)] for j in range(rows)]
board[0][0] = 'Q1'
board[1][4] = 'Q2'
board[1][6] = 'Q3'
board[2][2] = 'Q4'
board[3][1] = 'Q5'
board[6][3] = 'Q6'
board[6][5] = 'Q7'
board[6][7] = 'Q8'

for i in range(cols):
    for j in range(rows):
        if board[i][j] != 'x':
            print(board[i][j], 'Attacks')
            # checking if there is a queen in row or column
            for k in range(8):
                if board[i][k] != board[i][j] and board[i][k] != 'x':
                    print(board[i][k])
                if board[k][j] != board[i][j] and board[k][j] != 'x':
                    print(board[k][j])
            # checking diagonals
            for l in range(8):
                for m in range(8):
                    if (l+m == i+j) or (l-m == i-j):
                        if board[l][m] != board[i][j] and board[l][m] != 'x':
                            print(board[l][m])
