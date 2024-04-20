import sys
input = sys.stdin.readline
n,m= map(int,input().split())
num = list(map(int,input().split()))
cnt = 0
cumsum, end = 0,0
for start in range(n):
    while cumsum <m and end <n:
        cumsum += num[end]
        end += 1
    if cumsum==m :
        cnt+=1
    cumsum -= num[start]

print(cnt)