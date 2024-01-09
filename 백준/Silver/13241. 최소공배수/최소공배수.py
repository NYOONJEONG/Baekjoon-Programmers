a, b = map(int, input().split())
output =[]
if a>b :
    for i in range(1,b+1):
        if (a*i) % b==0 :
            output.append(a*i)
        else : pass
else : 
    for j in range(1,a+1):
        if (b*j)%a==0 :
            output.append(b*j)
        else : pass
print(min(output))