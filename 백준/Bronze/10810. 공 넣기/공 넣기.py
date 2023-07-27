N, M = map(int, input().split())
B = [0 for _ in range(N)]

for _ in range(M):
    i,j,k = map(int, input().split())
    for n in range(i,j+1):
        B[n-1] = k

for n in range(N):
    print(B[n], end = ' ')