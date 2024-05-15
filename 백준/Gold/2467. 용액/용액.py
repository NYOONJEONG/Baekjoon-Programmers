import sys
input = sys.stdin.readline
n = int(input())
liquid = list(map(int, input().split()))
check = 2000000001
output= []
x,y = 0,0
s = 0
e = n-1

while s<e:
    tmp = liquid[s]+liquid[e]
    if abs(tmp) <= abs(check) :
        x= liquid[s]
        y = liquid[e]
        check = tmp
    
    if tmp <= 0:
        s += 1
    else: 
        e -= 1
print(x,y)