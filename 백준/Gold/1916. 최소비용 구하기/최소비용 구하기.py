import heapq
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[ ] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
start , end = map(int, input().split())

def dijkstra(start):
    INF = int(1e9)
    distance = [INF] * (n+1)    
    q= []
    heapq.heappush(q, (0,start))
    distance[start] = 0 
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for node_index, node_cost in graph[now]:
            cost = dist + node_cost

            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))
    return distance

result = dijkstra(start)
print(result[end])