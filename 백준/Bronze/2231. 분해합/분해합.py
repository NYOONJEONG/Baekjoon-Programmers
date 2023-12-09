N = int(input())
for i in range(N):
    num = sum(map(int, str(i)))
    result = i + num
    if result == N :
        print(i)
        break 
else : print(0)