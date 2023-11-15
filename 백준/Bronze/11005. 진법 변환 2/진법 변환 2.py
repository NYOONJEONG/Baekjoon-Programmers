N, B = map(int, input().split())
num="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
output=''
while N != 0:
    output += str(num[N%B])
    N = N//B

print(output[::-1])