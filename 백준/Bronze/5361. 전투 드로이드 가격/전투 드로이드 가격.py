n = int(input())
price = [350.34,230.90,190.55,125.30,180.90]

for _ in range(n):
    num_list = list(map(int,input().split()))
    total = 0
    for i in range(5):
        total += price[i]*num_list[i]
    print('$', f"{total:.2f} ", sep='')
