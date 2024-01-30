import sys
N,M = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))

start = 0 
end = max(height)
while start <= end : 
    total =0
    mid = (start+end)//2
    for i in height:
        if i > mid:
            total += i -mid
    if total < M :
        end = mid-1
    else: 
        start = mid+ 1
print(end)