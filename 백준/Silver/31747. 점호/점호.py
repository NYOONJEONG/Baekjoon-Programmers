import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())
a = list(map(int,input().split()))
d = deque(a)
t = 0
while d:
    p = len(d)
    m = min(p,k)
    # print(m)
    one, two = False, False
    plus = []
    # print(d,'0')
    t += 1

    for _ in range(m):
        x = d.popleft()
        if x ==1 and one==False:
            one=True
            # print(d,'1')
            
        elif x==2 and two == False:
            two = True
            # print(d,'2')
        
        elif one == True or two == True:
            plus.append(x)

    d.extendleft(plus)
    # print(d, '3', t)
print(t)