n = int(input())
m = int(input())
graph = [set() for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].add(end)
    graph[end].add(start)  
    
for i in range(n+1):
    graph[i] = list(graph[i])

count= 0
def dfs(graph, v, visited) :
    global count
    visited[v] = True
    count += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i, visited)
visited=[False]*(n+ 1)
dfs(graph, 1, visited)
print(count-1)