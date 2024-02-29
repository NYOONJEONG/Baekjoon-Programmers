import sys
input =sys.stdin.readline
n = int(input())
ans = [0]* (1000001)

ans[1] = 1
ans[2]= 2

for i in range(3,n+1):
    ans[i]= (ans[i-1]+ ans[i-2])%15746

print(ans[n])