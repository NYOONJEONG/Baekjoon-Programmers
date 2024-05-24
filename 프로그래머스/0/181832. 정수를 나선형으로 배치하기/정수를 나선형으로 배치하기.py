def solution(n):
    answer = [[0]*n for _ in range(n)]
    # moves = [(1,0),(0,-1),(-1,0),(0,1)]
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x,y = 0,0
    answer[x][y] = 1

    d = 0
    for i in range(2,n*n+1):
        nx= x+moves[d][0]
        ny = y+moves[d][1]
        
        if 0<=nx<n and 0<=ny<n and answer[nx][ny]==0:
            answer[nx][ny]=i
            x,y= nx,ny
            
        else :
            d = (d+1)%4
            nx = x + moves[d][0]
            ny = y + moves[d][1]
            answer[nx][ny]= i
            x,y=nx,ny
    return answer