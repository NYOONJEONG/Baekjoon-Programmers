import sys
input = sys.stdin.readline
n= int(input())
num = list(map(int, input().split()))
dp = []
dp.append(num[0])
for i in range(1,n):
    dp.append(max(dp[i-1]+ num[i], num[i]))
print(max(dp))