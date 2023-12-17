import sys
N = sorted(list(str(input())))
out = []
for i in N :
    out.append(int(i))
output=0
for i in range(len(out)):
    output += out[i] * 10**i
print(output)