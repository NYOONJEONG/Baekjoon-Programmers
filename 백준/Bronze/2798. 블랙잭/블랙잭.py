N , M = map(int, input().split())
num = sorted(map(int, input().split()))
answer = []
for i in range(N) :
    for j in range(i+1,N):
        for k in range(j+1,N):
            if num[i]+ num[j]+num[k] <= M : answer.append(num[i]+ num[j]+num[k])
print(max(sorted(answer)))