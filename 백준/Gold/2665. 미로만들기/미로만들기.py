from collections import deque
import sys
input = sys.stdin.readline

n= int(input())
graph = []
for i in range(n):
    graph.append(list(str(input())))

move = [(0,1),(1,0),(-1,0),(0,-1)]

def bfs():
    q = deque([(0,0)]) 
    visited = [[-1] * n for _ in range(n)]
    visited[0][0] = 0
    answer = []

    while q:
        x, y = q.popleft()

        if x==n-1 and y==n-1:
            return visited[x][y]
        
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny]==-1:
                if graph[nx][ny] == '1':
                    q.appendleft((nx,ny))
                    visited[nx][ny] = visited[x][y]

                else : 
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
                

print(bfs())