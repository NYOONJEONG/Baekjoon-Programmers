T = int(input())
dp = [0] * 101
for _ in range(T):
    n = int(input())
    if n <= 3 : print(1)
    elif n==4 or n==5 : print(2)
    else : 
        dp = [0] * 101
        dp[1],dp[2], dp[3] = 1,1,1
        dp[4] , dp[5] = 2,2

        for  i in range(6,n+1) :
            dp[i] = dp[i-5]+ dp[i-1]
        print(dp[n])