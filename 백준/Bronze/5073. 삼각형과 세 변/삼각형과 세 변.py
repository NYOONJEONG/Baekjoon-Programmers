while True :
    a,b,c = map(int, input().split())
    length= sorted([a,b,c])
    if a==b==c==0 : break 
    elif length[2] >= length[0]+ length[1] : print("Invalid")
    elif a==b==c : print("Equilateral")
    elif (a==b) or (a==c) or (b==c) : print("Isosceles")
    else : print("Scalene")