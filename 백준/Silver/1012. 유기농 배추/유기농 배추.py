import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())
result = []

def dfs(x,y):
  if x<0 or y<0 or x>=n or y>=m: #범위를 초과하는 경우
    return  #종료조건
    
  if graph[x][y]==1: #범위를 초과하지 않고 배추인 경우
    graph[x][y] = 0
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)

for _ in range(t):
    m,n,k = map(int, input().split()) # m은 x. n기 y
    graph = [[ 0 for i in range(m) ] for j in range(n)]
    visited = [[0 for i in range(m) ] for j in range(n)]
    for _ in range(k):
        x,y=  map(int, input().split())
        graph[y][x] = 1

    
    anw = 0

    for i in range(n):#y
        for j in range(m): #x
            if graph[i][j] and not visited[i][j]:
                dfs(i,j)
                anw += 1
    result.append(anw)

for answer in result :
    print(answer)