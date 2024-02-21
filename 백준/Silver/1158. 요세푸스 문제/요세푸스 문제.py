n,k = map(int, input().split())
remove_index = 0 
num_list = []
remove_list = []
for i in range(n):
    num_list.append(i+1)

while len(num_list) >0 :
    remove_index = (remove_index + (k-1))%len(num_list)
    remove = num_list.pop(remove_index)
    remove_list.append(remove)
print("<", end='')
for x in remove_list[:-1]:
    print(x, end= ', ')
print(remove_list[-1], end='')
print(">", end=" ")