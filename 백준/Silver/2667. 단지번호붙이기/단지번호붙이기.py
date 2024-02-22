n = int(input())
graph = [set() for _ in range(n+1)]
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    global num

    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        num += 1

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

ans =  []
for i in range(n):
    for j in range(n):
        num = 0
        if dfs(i, j) == True:
            ans.append(num)

print(len(ans))
print('\n'.join(map(str, sorted(ans))))