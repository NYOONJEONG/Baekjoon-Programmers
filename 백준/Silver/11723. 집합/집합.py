import sys
input = sys.stdin.readline
n = int(input())
S = set()
for _ in range(n):
    tmp = input().split()
    if len(tmp)==2 :
        action, x = tmp[0],int(tmp[1])
    else : action= tmp[0]

    if action == 'add' :
        S.add(x)
    elif action =='remove':
        S.discard(x)
    elif action=='check':
        if x in S :
            print(1)
        else: print(0)
    elif action=='toggle':
        if x in S:
            S.discard(x)
        else : S.add(x)
    elif action=="all":
        S = set([i for i in range(1,21)])
    elif action=='empty': 
        S = set()