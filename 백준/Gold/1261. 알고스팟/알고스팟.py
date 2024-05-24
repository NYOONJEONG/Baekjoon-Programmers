import heapq
import sys
input = sys.stdin.readline

m,n = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
    
def bfs():
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while q :
        cnt, x,y = heapq.heappop(q)
        visited[x][y] =1
        if x==n-1 and y==m-1:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny]= 1

                if graph[nx][ny] == '0' :
                    heapq.heappush(q,(cnt,nx,ny))

                else :
                    heapq.heappush(q,(cnt+1, nx,ny))
                    
visited = [[0]*m for i in range(n)]
q = []
heapq.heappush(q,(0,0,0))
print(bfs())