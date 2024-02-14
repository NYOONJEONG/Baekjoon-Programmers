import sys
n =int(sys.stdin.readline())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

third = {}
for x in num:
    if x in third:
        third[x] += 1
    else:
        third[x] = 1
mode = sorted(third.items(), key=lambda x: x[1],reverse=True)

print(int(round(sum(num)/n,0))) # 산술평균
print(num[n//2])# 중앙값

if n==1 : print(mode[0][0])
elif mode[0][1]==mode[1][1] : print(mode[1][0])
else : print(mode[0][0]) # 최빈값

print(int(num[n-1]-num[0])) # 범위