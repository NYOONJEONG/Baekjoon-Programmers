from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
r,c,d = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)] # (북, 동, 남, 서 순서)

def turn_left(direction):
    return (direction + 3) % 4

def bfs(x,y,d):
    global cnt
    visited[x][y] = True
    q = deque()
    q.append((x,y,d))
    cnt +=1
    
    while q:
        x, y,d = q.popleft()
        cleaned = False
        for _ in range(4):
            d = turn_left(d)
            nx,ny = x+moves[d][0], y+moves[d][1]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny]==0:
                visited[nx][ny]=True
                cnt +=1
                q.append((nx,ny,d))
                cleaned = True
                break
        if not cleaned : 
            bx = x-moves[d][0]
            by = y-moves[d][1]
            if 0<=bx<n and 0<=by<m and graph[bx][by]==0:
                q.append((bx,by,d))
            else :
                return
visited = [[False]*m for _ in range(n)]
cnt= 0
bfs(r,c,d)
print(cnt)