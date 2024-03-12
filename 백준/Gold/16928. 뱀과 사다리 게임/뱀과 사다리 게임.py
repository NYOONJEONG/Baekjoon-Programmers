from collections import deque
n, m = map(int, input().split())

board = [0] * 101
visited = [False] * 101
 
up= dict()
for _ in range(n):
    i,j = map(int,input().split())
    up[i] = j

down = dict()
for _ in range(m):
    i,j = map(int,input().split())
    down[i] = j
    
def bfs(start) : 
    q= deque()
    q.append(start)

    visited[start] = True

    while q:
        x = q.popleft()

        for i in range(1,7):
            nx = x + i
            
            if 0<nx<=100 and not visited[nx] :
                if nx in up:
                    nx = up[nx]
                
                if nx in down:
                    nx = down[nx]
                    
                if not visited[nx]:
                    q.append(nx)
                    visited[nx]= True
                    board[nx] = board[x] +1
bfs(1)
print(board[100])