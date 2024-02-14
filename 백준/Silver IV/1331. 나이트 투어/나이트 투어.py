alphabet = ['A','B','C','D','E','F']
path=[]
import sys
for i in range(36):    
    point = list(sys.stdin.readline())
    x,y= alphabet.index(point[0])+1, int(point[1])
    path.append((x,y))
path.append(path[0])
wrong=0
for i in range(36):
    if abs(path[i][0]-path[i+1][0])==2 and abs(path[i][1]-path[i+1][1])==1 : pass
    elif abs(path[i][0]-path[i+1][0])==1 and abs(path[i][1]-path[i+1][1])==2 : pass
    else : 
        wrong += 1
check =[]
wrong_final = 0
for x in path:
    if x not in check : check.append(x)
    else : wrong_final +=1
if wrong!=0 or wrong_final>1 : print("Invalid")
else : print("Valid")