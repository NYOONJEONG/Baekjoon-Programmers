import heapq
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
heap =[]
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1,n+1):
    if indegree[i]==0:
        heapq.heappush(heap,i)

while heap :
    value = heapq.heappop(heap)
    result.append(value)
    for i in graph[value]:
        indegree[i] -= 1
        if indegree[i]==0:
            heapq.heappush(heap,i)

for i in result:
    print(i,end=" ")
