import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
S = list(map(int,input().split()))
num = [0] * (max(S)+1)

def fruit():
    start, end, cnt, kind, max_val = 0, 0, 0, 0, 0
    while end < n:
        if num[S[end]] == 0:
            kind += 1
        
        cnt += 1
        num[S[end]] += 1
        
        while kind > 2:
            if num[S[start]] == 1:
                kind -= 1
            num[S[start]] -= 1
            cnt -= 1
            start += 1
        
        max_val = max(max_val, cnt)
        end += 1
    
    return max_val

print(fruit())