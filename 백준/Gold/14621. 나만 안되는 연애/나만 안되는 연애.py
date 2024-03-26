import sys
input = sys.stdin.readline
def find_parent(parent, x):
    if parent[x]!=x :
        parent[x]= find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b= find_parent(parent, b)
    if a<b:
        parent[b]= a
    else: 
        parent[a]=b

n,m = map(int, input().split())
gender = [''] + list(input().split())
edges = []
result = 0
for _ in range(m):
    a,b,d = map(int, input().split())
    edges.append((d, a, b))

parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i]= i

edges.sort()

for dist, a, b in edges :
    if find_parent(parent,a) != find_parent(parent,b) and gender[a]!= gender[b]:
        union_parent(parent, a,b)
        result += dist
        
print(result if len([i for i in range(1, n+1) if parent[i] == i]) == 1 else -1)