import sys
from collections import deque
n = int(sys.stdin.readline())
num = deque()
for i in range(1,n+1):
    num.append(i)

while len(num)>1 :
    num.popleft()
    num.append(num.popleft())
print(num[0])