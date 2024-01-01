N = int(input())
five = N//5
output =[]
for i in range(five+1):
    three = (N-5*i)//3
    if (N-5*i)%3 ==0 : output.append(three+i)
    else : pass
if output == [] : print(-1)
else : print(min(output))