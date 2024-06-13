import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
S = list(map(int,input().split()))
num = [0] * (max(S)+1)

def fruit(start, end, cnt, kind, max_val):
    global num

    if end >= n:
        return max_val 

    if num[S[end]] == 0:
        kind += 1

    cnt += 1 
    num[S[end]] += 1 
    
    if kind > 2: 
        if num[S[start]] == 1: 
            kind -= 1
        num[S[start]] -= 1
        cnt -= 1 
        start += 1 

    max_val = max(max_val, cnt) 

    return fruit(start, end + 1, cnt, kind, max_val) 

print(fruit(0, 0, 0, 0, 0))