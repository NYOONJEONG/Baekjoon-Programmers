import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

cnt = 0
def new_point(before, n):
    return before-2**(n-1)

def z(n,r,c):
    if n==1 :
        return 2*r+c
    
    # 2사분면
    if r<2**(n-1) and c<2**(n-1):
        return z(n-1,r,c)
    
    # 1사분면
    elif r<2**(n-1) and c>= 2**(n-1):
        return 2**(2*n-2) + z(n-1, r, new_point(c,n))
    
    # 3사분면
    elif r >= 2**(n-1) and c<2**(n-1):
        return 2**(2*n-1) + z(n-1, new_point(r,n), c)
    
    # 4사분면
    else : 
        return 3*2**(2*n-2) + z(n-1,new_point(r,n), new_point(c,n))

print(z(n,r,c))