import sys
input = sys.stdin.readline
n = int(input())
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))
dp = [[0]*3 for i in range(n)]

for i in range(3):
    dp[0][i] = cost[0][i]
for i in range(1,n):
    for j in range(3):
        minimum = 1000 * 1000
        for k in range(3):
            if j==k :
                continue
            if dp[i-1][k] < minimum:
                minimum = dp[i-1][k]
            dp[i][j] = minimum + cost[i][j]
print(min(dp[n-1]))