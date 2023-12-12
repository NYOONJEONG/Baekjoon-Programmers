N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))

result = sorted(num)
for i in range(N):
    print(result[i])