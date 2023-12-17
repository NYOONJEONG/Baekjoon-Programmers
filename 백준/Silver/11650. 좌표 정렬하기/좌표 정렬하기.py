import sys
N = int(sys.stdin.readline())
xy = []
for i in range(N):
    a,b = map(int,sys.stdin.readline().split())
    xy.append([a,b])
xy.sort()
for i in xy:
    print(i[0],i[1])