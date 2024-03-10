import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = list(input())
anw = 0
for i in range(m-(2*n)):
    if s[i]=='I' :
        cnt = 0
        for j in range(1,n+1):
            if s[i+2*j-1]!='O' or s[i+2*j]!='I': cnt += 1
        if cnt ==  0 : 
            anw += 1
print(anw)