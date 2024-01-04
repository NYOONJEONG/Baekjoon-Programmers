N = int(input())
order = []
for i in range(N):
    age, name = input().split()
    order.append([int(age), name])

for i in sorted(order, key=lambda x : x[0]) :
    print(i[0],i[1])