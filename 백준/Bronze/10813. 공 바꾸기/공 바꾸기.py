N, M = map(int, input().split())
B = [i for i in range(1,N+1)]
temp =0

for i in range(M):
    i,j = map(int, input().split())
    temp=B[i-1]
    B[i-1]= B[j-1]
    B[j-1] = temp

for i in range(N):
    print(B[i], end = ' ')