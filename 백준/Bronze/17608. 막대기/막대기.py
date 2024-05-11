import sys
input = sys.stdin.readline
n = int(input())
block  = []
for _ in range(n):
    x = int(input())
    if len(block)!=0:
        while block[-1]<=x:
            block.pop()
            if len(block)==0 :
                break
        block.append(x)
    else : 
        block.append(x)
print(len(block))