import sys
input = sys.stdin.readline
n,k = map(int,input().split())
a = list(map(int,input().split()))

cnt = {1:0, 2:0}
for x in a[:k]:
    cnt[x] += 1
if n==k :
    print(max(cnt[1], cnt[2]))
else :
    t = 0
    start = 0
    while start <= n:
        if min(cnt[1],cnt[2])==0:
            if cnt[1] ==0:
                cnt[2] -= 1
            else:
                cnt[1] -= 1
            
            if start + k < n:
                cnt[a[start+k]] += 1
            
            start += 1

        else :
            cnt[1] -= 1
            cnt[2] -= 1
            if start +k <n :
                cnt[a[start+k]] += 1
            if start + k + 1 < n:
                cnt[a[start+k+1]] += 1
        
            start += 2
        t += 1
    print(t-1)