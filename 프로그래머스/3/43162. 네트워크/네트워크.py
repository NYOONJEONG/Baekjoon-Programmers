import sys
sys.setrecursionlimit(10**6)

def solution(n, computers):
    answer = 0
    visited = [False]*(n)
    
    def dfs(i, n, visited, computers) :
        for j in range(n):
            if i!=j and computers[i][j] == 1 and not visited[j] :
                visited[j]=True
                dfs(j, n, visited, computers)
            
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer += 1
            dfs(i, n, visited, computers)
            
    return answer