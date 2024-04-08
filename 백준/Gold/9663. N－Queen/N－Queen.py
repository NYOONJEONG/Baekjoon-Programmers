N = int(input())
board = [0] * N
cnt = 0

def board_check(pos):
    for idx in range(pos):
        if  board[pos]==board[idx] or abs(pos - idx) == abs(board[pos]-board[idx]):
            return False
    return True


def create_board(pos, N):
    value = 0
    global cnt

    if pos == N:
        cnt += 1
        return 1
    
    while value < N:
        board[pos] = value
        if board_check(pos) == 1:
            create_board(pos + 1, N)
        value += 1

create_board(0, N)
print(cnt)