import sys
T =int(sys.stdin.readline())
for _ in range(T):

    a,b=map(int,sys.stdin.readline().split())
    num=a%10

    if num==0:
        print(10)
    elif num==1 or num==5 or num==6:
        print(num )
    elif num==4 or num==9:
        if b%2==0:
            print((num**2)%10)
        else:
            print(num)
    else:
        if b%4==0:
            print(num**4%10)
        else:
            print(num**(b%4)%10)   