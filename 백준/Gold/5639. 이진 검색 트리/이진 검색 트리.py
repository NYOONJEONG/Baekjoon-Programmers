import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

tree = []
while True:
    try :
        x= int(input())
        tree.append(x)
    except :
        break

def find_tree(Tree):
    if len(Tree)==0:
        return
    L,R= [], []
    mid = Tree[0]

    for i in range(1,len(Tree)):
        if Tree[i]>mid :
            L= Tree[1:i]
            R = Tree[i:]
            break
    else :
        L = Tree[1:]
    find_tree(L)
    find_tree(R)
    print(mid)
    
find_tree(tree)