n, m = map(int, input().split())
board = []
last_cnt = 64

def board_check(board):
    w_cnt = 0
    r_cnt = 0

    for i in range(8):
        for j in range(8):
            if (j+i) % 2 == 0:
                if board[i][j] == 'B':
                    w_cnt += 1
            else:
                if board[i][j] == 'W':
                    w_cnt += 1

    for i in range(8):
        for j in range(8):
            if (j+i) % 2 == 0:
                if board[i][j] == 'W':
                    r_cnt += 1
            else:
                if board[i][j] == 'B':
                    r_cnt += 1
    return min(w_cnt, r_cnt)

for i in range(n):
    board.append(list(input()))

for i in range(n-8 + 1):
    for j in range(m-8 + 1):
        new_board = [[0]*8 for _ in range(8)]
        for k in range(8):
            for l in range(8):
                new_board[k][l] = board[i+k][j+l]

        last_cnt = min(last_cnt, board_check(new_board))
print(last_cnt)