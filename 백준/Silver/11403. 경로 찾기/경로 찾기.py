n = int(input())
G = [list(map(int, input().split())) for i in range(n)]
for k in range(0, n) :
    for i in range(0, n) :
        for j in range(0, n):
            if G[i][k] and G[k][j] :
                G[i][j] = 1
 
for i in range(0, n) :
    _str = ""
    for j in range(0, n) :
        _str += str(G[i][j]) +  " "
    print(_str)