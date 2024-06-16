n = int(input())
dp=[-1]*(n+1)

dp[1]= 1 #SK
if n==1:
    print('SK')
elif n==2:
    print('CY')
elif n==3:
    print('SK')
else : 
    dp[2] = 0 # CY
    dp[3] = 1 #SK

    for i in range(4,n+1):
        if dp[i-1]== 1 or dp[i-3]==1 :
            dp[i]=0
        else:
            dp[i]=1

    if dp[n]==1:
        print('SK')
    else: 
        print('CY')