import sys
N = int(sys.stdin.readline())
budget = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

start = 0
end=max(budget)
result = 0

while start<=end:
    total = 0
    mid = (start+end)//2
    for x in budget :
        if x > mid : total += mid
        else : total += x 
    if total <= M :
        result = mid 
        start = mid +1
    else : end = mid-1
print(result)