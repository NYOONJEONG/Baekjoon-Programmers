import sys
input = sys.stdin.readline
n,m= map(int,input().split())
num = list(map(int,input().split()))
cnt = 0
cumsum, right = 0,0
for i in range(n):
    while cumsum <m and right <n:
        cumsum += num[right]
        right += 1
    if cumsum==m :
        cnt+=1
    cumsum -= num[i]

print(cnt)