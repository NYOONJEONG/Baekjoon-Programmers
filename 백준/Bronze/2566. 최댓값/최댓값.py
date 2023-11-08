maxN = 0
nrow = 1
ncol = 1

for i in range(9):
    N = list(map(int, input().split()))
    if max(N)> maxN :
        maxN = max(N)
        nrow = i+1
        ncol = N.index(maxN) + 1

print(maxN)
print(nrow, ncol)