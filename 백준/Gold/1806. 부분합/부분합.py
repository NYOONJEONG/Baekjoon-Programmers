import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = list(map(int,input().split()))

min_length = float('inf')
current_sum = 0
start = 0

for end in range(n):
    current_sum += arr[end]

    while current_sum >= m:
        min_length = min(min_length, end - start + 1)
        current_sum -= arr[start]
        start += 1

if min_length == float('inf'):
    print(0)
else:
    print(min_length)