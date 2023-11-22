n, k = map(int, input().split())
num = []
for i in range(1, n+1):
    if n%i==0:
        num.append(i)
    else : pass

if len(num)>=k : 
    answer = num[k-1]
else : answer = 0
print(answer)