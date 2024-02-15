a,b,v = map(int, input().split())
climb = v-a
day = (v-a)//(a-b)
for _ in range(v):
    climb += a
    day += 1
    if climb >= v : break
    else : climb -= b

if (v-a)/(a-b)==int((v-a)/(a-b)) : print(day)
else : print(day+1)
