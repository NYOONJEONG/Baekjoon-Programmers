import sys
input = sys.stdin.readline
n =int(input())
while True:
    check = True
    for x in str(n):
        if x != '4' and x != '7':
            check = False
            n -=1
    
    if check :
        print(n)
        break