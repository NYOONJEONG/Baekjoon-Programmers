import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
visited = [0] * n 
cnt, find = [], []

def dfs(depth):
    if depth == n:
        cnt.append(sum(abs(find[i]- find[i-1]) for i in range(n-1)))
        return
    
    for i in range(n):
        if visited[i] :
            continue
        find.append(num[i])
        visited[i]=1
        dfs(depth+1)

        visited[i]=0
        find.pop()
dfs(0)
print(max(cnt))