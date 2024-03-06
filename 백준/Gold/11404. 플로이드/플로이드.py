import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
G = [[INF] *(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            G[a][b]=0

for _ in range(m):
    a,b,c = map(int, input().split())
    if G[a][b] == INF : 
        G[a][b]=c
    else : G[a][b] = min(G[a][b], c)

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            G[a][b]= min(G[a][b], G[a][k]+G[k][b])
for i in range(1, n+1) :
    output = ""
    for j in range(1, n+1) :
        if G[i][j]== INF : 
            G[i][j]=0
        output += str(G[i][j]) +  " "
    print(output)