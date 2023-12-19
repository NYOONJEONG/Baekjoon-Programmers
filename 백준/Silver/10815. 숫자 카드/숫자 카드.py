N = int(input())
have = list(map(int, input().split()))
M = int(input())
check = list(map(int,input().split()))
output = {}

for i in check:
    output[i] = 0

for j in have:
    if j in output:
        output[j] = 1

for k in output:
    print(output[k], end=' ')