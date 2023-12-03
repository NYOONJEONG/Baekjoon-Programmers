a,b,c = sorted(map(int, input().split()))
if c < a+b :
    sum_round = a+b+c
else : sum_round = a+b+min(c, a+b-1)
print(sum_round)