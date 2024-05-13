import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = []
for _ in range(n) :
    board.append(list(map(int, input().split())))

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x,y, sum, depth):
    global output
    if depth == 4 :
        output = max(output, sum)
        return
    
    for i in range(4):
            nx = move[i][0] + x
            ny = move[i][1] + y
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                 visited[nx][ny]= 1
                 dfs(nx,ny, sum+ board[nx][ny], depth+1)
                 visited[nx][ny] = 0

def dfs2(x,y):
    global output
    for i in range(4):

        tmp = board[x][y] # 시작값

        for k in range(3):
            # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301
            t = (i+k)%4
            nx = x+move[t][0]
            ny = y+move[t][1]

            if not (0 <= nx <n and 0<=ny <m):
                tmp = 0
                break
        
            tmp += board[nx][ny]

        output = max(output, tmp)
output = 0
visited = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] =1
        dfs(i,j,board[i][j], 1)
        visited[i][j] = 0

        dfs2(i,j)

print(output)