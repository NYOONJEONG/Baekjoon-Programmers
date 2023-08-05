num = []
for _ in range(10):
    x = int(input())
    y= x%42
    num.append(y)

print(len(set(num)))
    