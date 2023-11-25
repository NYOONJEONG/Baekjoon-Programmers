M = int(input())
N = int(input())

not_prime = []
num = []

for i in range(M, N+1) :
    if i > 1: 
        num.append(i)
        for j in range(2,i):
            if i%j==0 : 
                not_prime.append(i)
                break

prime = set(num)-set(not_prime)

if len(prime)==0 : 
    print("-1")
else:
    print(sum(prime))
    print(min(prime))