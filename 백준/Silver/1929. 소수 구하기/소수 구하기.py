M, N = map(int, input().split())
def prime_list(m,n):
    sieve = [True] * n
    k = int(n ** 0.5)
    for i in range(2, k + 1):
        if sieve[i] == True:           
            for j in range(i+i, n, i): 
                sieve[j] = False
    return [i for i in range(m, n) if sieve[i] == True]

if M != 1:
    for x in prime_list(M,N+1) :
        print(int(x))
else : 
    for x in set(prime_list(M,N+1)) - {1} :
        print(x)
