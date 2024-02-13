N = int(input())
def VPS(vps_input):
    start =[]
    end = []
    for i in range(len(vps_input)):
        if vps_input[i] == "(":
            start.append(i)
        else : end.append(i)
    
    if len(start)!= len(end) :
        print("NO")
    else : 
        count = 0
        for i in range(len(start)):
            if start[i]< end[i] : pass
            else: count += 1
        if count!=0 : print("NO")
        else : print("YES")

for _ in range(N):
    vps_input = input()
    VPS(vps_input)     