n=int(input())
step= []
for _ in range(n):
    step.append(int(input()))

if n>2:
    d= [0]*300

    d[0]= step[0]
    d[1]= step[0]+ step[1]
    d[2]= max(step[0]+step[2], step[1]+step[2])

    for i in range(2,n) :
        d[i]= max(d[i-3]+ step[i-1]+step[i], d[i-2]+step[i])
    print(d[n-1])
else : print(sum(step))