while True :
    num = list(input())
    if num==['0']: break
    cnt=0
    n = len(num)

    for i in range(n):
        if num[i]==num[n-i-1] : pass
        else: cnt += 1

    if cnt == 0: 
        print('yes')
    else: print('no')