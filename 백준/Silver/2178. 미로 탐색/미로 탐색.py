from collections import deque
import sys
imput = sys.stdin.readline

n,m = map(int, input().split())
graph = []
for i in range(n):
    numbers=list(input())
    num = []
    for j in range(m):
        num.append(int(numbers[j]))
    graph.append(num)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append([x,y])

    while q:
        now = q.popleft()
        
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if nx >= 0 and nx<n and ny >= 0 and ny < m:

                if graph[nx][ny]==1  :

                    graph[nx][ny] = graph[now[0]][now[1]] +1
                    q.append([nx,ny])

bfs(0,0)
print(graph[n-1][m-1])