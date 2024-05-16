from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for x in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j]==9:
            x,y= i,j
move = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(time,x,y):
    visited=[[0 for _ in range(n)]for _ in range(n)]
    ate = []

    queue = deque()
    queue.append([time,x,y])
    visited[x][y] = 1

    while queue:
        time,x,y = queue.popleft()
        
        for i in range(4):
            nx = move[i][0] + x
            ny = move[i][1] + y
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny]==0:
                if board[nx][ny]==0 or board[nx][ny]==size :
                    queue.append([time+1,nx,ny])
                    visited[nx][ny]=1
                elif 0<board[nx][ny]<size:
                    ate.append([time+1,nx,ny])
                    visited[nx][ny]= 1
    if len(ate)==0:
        return False
    else : 
        return sorted(ate)

fish = 0
size= 2
time = 0
while True:
    board[x][y]=0
    output = bfs(0,x,y)
    if output == False :
        print(time)
        break
    fish += 1
    if size == fish :
        size +=1
        fish = 0

    x= output[0][1]
    y = output[0][2]
    time += output[0][0]