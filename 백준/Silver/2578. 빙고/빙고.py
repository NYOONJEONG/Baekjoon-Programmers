import sys
input = sys.stdin.readline

def garo(visited):
    tmp = 0
    for row in visited:
        if sum(row)==5:
            tmp += 1
    return tmp

def sero(visited):
    tmp = 0
    v= list(map(list, zip(*visited)))
    for col in v:
        if sum(col)==5:
            tmp +=1
    return tmp

def right_left(visited):
    tmp = 0
    for i in range(5):
        if visited[i][i]!=1:
            return 0
    return 1

def left_right(visited):
    tmp = 0
    for i in range(5):
        if visited[i][4-i]!=1:
            return 0
    return 1
            
def bingo(call, visited):
    for i in range(5):
        for j in range(5):
            if board[i][j]==call:
                visited[i][j]=1
                break
    g = garo(visited)
    s = sero(visited)
    r =right_left(visited)
    l= left_right(visited) 

    if g+s+r+l >= 3:
        return 1
    else : 
        return 0
board = []
called = []
for _ in range(5):
    board.append(list(map(int, input().split())))
for _ in range(5):
    called.append(list(map(int, input().split())))
visited = [[0]*5 for i in range(5)]
cnt = 0
for i in range(5):
    for j in range(5):
        call = called[i][j]
        output = bingo(call, visited)
        cnt += 1
        if output == 1:
            break
    if output == 1:
        break
print(cnt)