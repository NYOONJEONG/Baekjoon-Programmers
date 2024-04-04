import sys
input = sys.stdin.readline

str_A = input().rstrip()
str_B = input().rstrip()
n = len(str_A)
m= len(str_B)
LCS = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if str_A[i-1]==str_B[j-1]:
            LCS[i][j] = LCS[i-1][j-1]+1
        else : 
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
print(max(max(LCS)))