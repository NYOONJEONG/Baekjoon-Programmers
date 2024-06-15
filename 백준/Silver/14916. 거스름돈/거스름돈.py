n= int(input())
cnt= 1e6

if n==1 :
    cnt= -1

if n%5==0:
    cnt = min(cnt,n//5)
if n%2==0:
    cnt = min(cnt,n//2)
    
if (n-n//5 *5)%2==0:
    cnt = min(cnt, n//5 + (n-n//5*5)//2)
elif n//5>0 and (n-(n//5-1)*5)%2==0 :
    cnt = min(cnt, n//5-1 + (n-(n//5-1)*5)//2)

if cnt!=1e6:
    print(cnt)
else:
    print(-1)    
