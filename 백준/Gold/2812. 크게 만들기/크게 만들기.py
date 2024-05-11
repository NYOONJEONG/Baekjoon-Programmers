import sys
input = sys.stdin.readline
n,k = map(int, input().split())
num_list = list(map(int, input().strip()))
result = []
cnt = k

for x in num_list :
    while result and cnt>0 and result[-1]<x:
        result.pop()
        cnt -= 1
    result.append(x)
    
if cnt > 0:
    result = result[:-cnt]  
for x in result:
    print(x, end="")