N = int(input())
factorial = 1
for i in range(1,N+1):
    factorial *= i
count = 0
for x in reversed(str(factorial)) :
    if int(x)==0 : 
        count += 1
    else: break
print(count)