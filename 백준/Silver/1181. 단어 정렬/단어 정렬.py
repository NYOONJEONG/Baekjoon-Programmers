N  = int(input())
output = []

for i in range(N):
    output.append(input())

set_list = list(set(output))
set_list.sort()
set_list.sort(key=len)

for i in set_list:
    print(i)