n,m,v = map(int,input().split())
graph = [set() for _ in range(n+1)]
from collections import deque
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].add(end)
    graph[end].add(start)  

for i in range(n+1):
    graph[i] = sorted(list(graph[i]))

def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]= True

visited_dfs=[False]* (n+1)
visited_bfs=[False]* (n+1)

dfs(graph, v, visited_dfs)
print(sep='\n')
bfs(graph, v, visited_bfs)