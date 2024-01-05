import sys
N = int(sys.stdin.readline())
X = list(map(int,sys.stdin.readline().split()))
X_sorted = sorted(list(set(X)))
dic = {X_sorted[i] : i for i in range(len(X_sorted))}
for i in X:
    print(dic[i], end=" ")