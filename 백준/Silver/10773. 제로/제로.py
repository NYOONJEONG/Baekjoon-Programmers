import sys
k = int(sys.stdin.readline())
num_list = []
for i in range(k):
    num = int(sys.stdin.readline())
    if num==0 : 
        num_list.pop()
    else :
        num_list.append(num)
print(sum(num_list))