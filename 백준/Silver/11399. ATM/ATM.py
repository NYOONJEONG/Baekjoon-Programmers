N =int(input())
time = sorted(map(int, input().split()))
total =0
for i in range(N):
    total += time[i]*(N-i)
print(total)