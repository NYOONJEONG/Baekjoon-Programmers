import sys
input = sys.stdin.readline

input_list = list(map(str,input()))
answer = 0
tmp = []

for idx in range(len(input_list)):  
    if input_list[idx] == '(':  
        tmp.append(input_list[idx])  

    elif input_list[idx] == ')':  
        if input_list[idx-1] == '(':  
            tmp.pop() 
            answer += len(tmp)

        elif input_list[idx-1] == ')':  
            tmp.pop()  
            answer += 1  
print(answer)