import sys
input = sys.stdin.readline

arr_A, arr_B = map(str, input().split())
n, m = len(arr_A), len(arr_B)
result = []
if n==m:
    cnt = 0
    for i in range(n):
        if arr_A[i]!=arr_B[i]:
            cnt += 1
    result.append(cnt)
else : 
    for i in range(m-n+1):
        cnt = 0
        for j in range(n):
            if arr_A[j]!=arr_B[i+j]:
                cnt +=1
        result.append(cnt)
print(min(result))