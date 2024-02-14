n = int(input())
xy = []
for _ in range(n):
    x,y = map(int, input().split())
    xy.append((x,y))
xy.sort(key= lambda x :(x[1], x[0]), reverse = False)
for x,y in xy :
    print(x,y ,sep=" ")