N = int(input())
A_list = set(map(int, input().split()))
M= int(input())
check = list(map(int, input().split()))

for x in check:
    if x in A_list:
        print(1)
    else : print(0)