n = int(input())
line = list(map(int, input().split()))

wait = []
cnt = 1 

while line :
    if line[0] == cnt :
        line.pop(0)
        cnt += 1
    else : 
        wait.append(line.pop(0))

    while wait :
        if wait[-1]== cnt :
            wait.pop()
            cnt += 1
        else : 
            break
if not wait :
    print("Nice")
else : 
    print("Sad")