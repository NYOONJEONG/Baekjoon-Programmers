import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for i in range(n):
    numbers=list(input())
    num = []
    for j in range(m):
        num.append(int(numbers[j]))
    graph.append(num)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
INF = int(1e9)

def bfs(x,y):
    global ans
    visit = set()
    q = deque()
    q.append([x,y,1,0])
    visit.add((0,0,0))
    if n==1 and m==1 :
        ans =1
        
    while q:
        x, y, cnt, dt = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx<n and ny >= 0 and ny < m and (nx,ny,dt) not in visit:
                if nx == n-1 and ny == m-1:
                    ans = min(ans, cnt+1)
                else : 
                    if graph[nx][ny]==0:
                        q.append((nx,ny,cnt+1, dt))
                        visit.add((nx,ny, dt))
                    elif graph[nx][ny] ==1 and dt == 0:
                        q.append((nx,ny,cnt+1,1))
                        visit.add((nx,ny,1))

ans = INF
bfs(0,0)
if ans == INF:
    print(-1)
else : print(ans)