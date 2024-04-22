import sys
input = sys.stdin.readline
n = list(input().strip())
output = ''
stack = []

for x in n:
    if x.isalpha() :
        output += (x)
    else : 
        if x == '(':
            stack.append(x)
        elif x=="*" or x=='/':
            while stack and (stack[-1]=="*" or stack[-1]=='/'):
                output += stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != "(":
                output += stack.pop()
            stack.pop()
while stack:
    output += (stack.pop())
print(output)