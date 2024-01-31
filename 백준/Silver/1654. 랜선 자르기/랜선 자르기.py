K, N = map(int, input().split())
height = []
for _ in range(K):
    height.append(int(input()))

start = 1
end = max(height)
while start <= end : 
    total =0
    mid = (start+end)//2
    for x in height:
         total += x//mid
    if total >=  N :
        start = mid +1
    else :
        end = mid-1

print(end)