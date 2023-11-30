N = int(input())
x_list = []
y_list= []
for i in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
x_set = set(x_list)
y_set = set(y_list)
if (len(x_set)==1) or (len(y_set)==1) : print(0)
else : print((max(x_set)-min(x_set))*(max(y_set)-min(y_set))) 