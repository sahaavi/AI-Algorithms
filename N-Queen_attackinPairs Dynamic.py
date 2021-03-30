# Number of queens
print("Enter the number of queens")
N = int(input())

# chessboard
# NxN matrix with all elements x
board = [['x']*N for _ in range(N)]
for b in range(N):
    print('---Give No.', b+1, 'Queen Position---')
    row = int(input("Enter row position: "))
    column = int(input("Enter column position: "))
    board[row][column] = 'Q'+str(b+1)

for i in range(N):
    for j in range(N):
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
