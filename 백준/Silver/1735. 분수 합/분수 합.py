def gcd(x,y): 
    mod = x % y
    while mod >0:
        x = y
        y = mod
        mod = x % y
    return y    

a, b = map(int, input().split())
c, d = map(int, input().split())
N = gcd(a*d + b*c, b*d) 
print((a*d + b*c)//N, b*d//N)