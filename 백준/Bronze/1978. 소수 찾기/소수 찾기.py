N = int(input())
num = map(int, input().split())
prime = 0
for i in num:
    error=0
    if i> 1: 
        for j in range(2, i):
            if i%j==0 :
                    error += 1
        if error ==0 :
             prime += 1
print(prime)