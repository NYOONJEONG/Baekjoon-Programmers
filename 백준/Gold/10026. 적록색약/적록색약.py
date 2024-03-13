import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
result = 0
rgb_result = 0
graph = []
for i in range(n):
    graph.append(list(input()))


dx = [-1,0,1,0]
dy = [0,-1,0,1]

def dfs(x,y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or ny >= n or nx<0 or ny <0 :
            continue
        if visited[nx][ny] == False and graph[x][y] == graph[nx][ny] :
            dfs(nx,ny)

visited = [[False]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False :
            dfs(i,j)
            result += 1

visited = [[False]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if visited[i][j] == False :
            dfs(i,j)
            rgb_result += 1

print(result, rgb_result)