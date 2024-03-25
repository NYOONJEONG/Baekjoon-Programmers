from collections import deque
import sys
input = sys.stdin.readline


n,m = map(int, input().split()) # n: 노드, m : 간선
degree = [0] * (n+1)
graph = [[] for i in range(n+1)]
result = []

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

def topo_sort():
    global result
    q = deque()

    for i in range(1, n+1):
        if degree[i] == 0 and len(result)<n and i not in result:
            q.append(i)

        
        while q :
            now = q.popleft()
            result.append(now)

            for i in graph[now]:
                degree[i] -= 1 # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기

                if degree[i]== 0:
                    q.append(i)


topo_sort()

for i in result :
    print(i, end=' ')
