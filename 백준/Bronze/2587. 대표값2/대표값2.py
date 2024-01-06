X = []
for _ in range(5):
    X.append(int(input()))
X.sort()
print(int(sum(X)/5))
print(X[2])