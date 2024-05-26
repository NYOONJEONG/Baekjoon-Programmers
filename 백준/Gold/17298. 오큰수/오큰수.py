import sys
input = sys.stdin.readline

n = int(input())
nge = list(map(int,input().split()))
place = [-1]*n
tmp = []
for idx in range(n):  
    while tmp and nge[tmp[-1]] < nge[idx]:  
        place[tmp.pop()] = nge[idx]  
    tmp.append(idx) 
print(*place)
