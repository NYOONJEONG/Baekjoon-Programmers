n = int(input())
num = [list(map(int,input().split())) for i in range(n)]
dp = [[0]*i for i in range(1,n+1)]
dp[0][0]= num[0][0]

for i in range(1,n):
    dp[i][0] = num[i][0]+ dp[i-1][0]
    dp[i][i]= num[i][i]+ dp[i-1][i-1]
    for j in range(1,i):
        dp[i][j]= num[i][j]+ max(dp[i-1][j-1],dp[i-1][j])
print(max(dp[n-1]))