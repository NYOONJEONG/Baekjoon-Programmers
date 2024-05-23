from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
row, col = map(int, input().split())
graph = []
for _ in range(row):
    graph.append(list(map(int, input().split())))
moves = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(start_x,start_y):
    visited = [[False]*col for _ in range(row)]
    max_depth = 0
    q = deque([(start_x, start_y, 0)]) 
    visited[start_x][start_y] = True
    # q = deque() 
    # q.append((start_x,start_y, 0))
    end_x , end_y= start_x,start_y

    while q:
        x,y, depth = q.popleft()
        if depth > max_depth :
            max_depth = depth
            end_x, end_y = x,y

        for move in moves:
            nx = x + move[0]
            ny = y + move[1]

            if 0<=nx<row and 0<=ny<col and not visited[nx][ny] and graph[nx][ny]!=0:
                visited[nx][ny]=True
                q.append((nx,ny, depth+1))
                    

    return graph[start_x][start_y], graph[end_x][end_y], max_depth

longest_depth = 0
max_sum= 0
for i in range(row):
    for j in range(col):
        if graph[i][j]!=0:
            start, end, depth = bfs(i,j)
            if depth > longest_depth :
                longest_depth = depth
                max_sum = start+end
            elif depth==longest_depth :
                max_sum = max(max_sum, start+end)

print(max_sum)