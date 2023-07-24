N,X = map(int,input().split())
A_list = list(map(int,input().split()))

for i in range(N):
    if X > A_list[i] :
        print(A_list[i], end=" ")
