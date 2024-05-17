import sys
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [list(map(int,input().split())) for x in range(n)]
chick = []
home = []
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 :
            home.append([i,j])
        elif graph[i][j]==2:
            chick.append([i,j])
            
def chicken_dist(home, chick):
    dist = 2*n+1
    for chicks in chick:
        tmp = abs(chicks[0] - home[0]) + abs(chicks[1] - home[1])
        if tmp<dist :
            dist = tmp
    return dist

def city_chick_dist(home, chick):
    city_dist = 0
    for city in home:
        city_dist += chicken_dist(city, chick)
    return city_dist 

cnt, output= [], 0

def dfs(depth, index, _cnt):
    global output
    if depth ==m :
        tmp2 = city_chick_dist(home,cnt)
        if not output or output>tmp2:
            output = tmp2
        return 
    for i in range(index, len(chick)):
        _cnt.append(chick[i])
        dfs(depth+1, i+1, cnt)
        _cnt.pop(-1)
    
dfs(0,0,cnt)
print(output)