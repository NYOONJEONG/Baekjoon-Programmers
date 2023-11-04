N= int(input())
for i in range(N):
    repeat, text = input().split()
    for j in text:
        print(j*int(repeat),end="")
    print()