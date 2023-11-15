N, B = input().split()
B = int(B)
output = 0
N_list = list(reversed(N))
num="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(N)):
    N_now = N_list[i]
    output += num.index(N_list[i])*(B**i)
print(output)