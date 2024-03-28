import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
q=deque()
for i in range(n):
    a=list(map(int,input().split()))
    graph.append(a)
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    for j in range(m):
        if graph[i][j] ==1 :
            q.append((i,j))
def bfs():
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==0  :
                    graph[nx][ny] = graph[x][y]+1
                    q.append([nx,ny])
bfs()
tmp = 0
flag = True

for lst in graph:
    for j in lst:
        if j==0:
            flag = False
            break
    tmp = max(tmp, max(lst))
if flag == True:
    print(tmp -1)
else : print(-1)