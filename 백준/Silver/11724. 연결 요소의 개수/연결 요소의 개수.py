import sys
sys.setrecursionlimit(10**6)
n, m= map(int, sys.stdin.readline().split())
graph = [ [i] for i in range(n+1)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visitied):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False]*(n+1)
cnt= 0

for i in range(1, n+1):
    if not visited[i]:
        cnt+= 1
        dfs(graph, i, visited)
print(cnt)