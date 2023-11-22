while (1):
    n = int(input())
    if n==-1 : break
    else: 
        num  = []
        for i in range(1, n):
            if n%i == 0 :
                num.append(i)
            else: pass
        if n == sum(num) :
            print(n, "=", end=" ")
            print(*num, sep=" + ")
        else : print("%d is NOT perfect." %n)