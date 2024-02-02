N = int(input())
k = int(input())
start , end =1, N*N
while start <= end :
    mid = (start+end)//2

    target =sum(min(mid//i, N) for i in range(1,N+1))

    if target >= k :
        end= mid-1
        output = mid
    else: start =mid +1
print(output)