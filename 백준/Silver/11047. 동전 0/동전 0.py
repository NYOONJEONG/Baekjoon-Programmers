import sys
N, K = map(int, sys.stdin.readline().split())
coin = []
for _ in range(N):
    coin.append(int(sys.stdin.readline()))
count = 0
for i in range(N): 
    while K//coin[N-i-1] > 0: 
        count += K//coin[N-i-1]
        K = K- (K//coin[N-i-1]) * coin[N-i-1]
print(count)