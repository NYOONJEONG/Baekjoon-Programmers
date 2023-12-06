a,b,c,d,e,f = map(int, input().split())
if b!=0 : 
    x= (c*e-f*b)/(a*e-d*b)
    y= (c-a*x)/b
else :
    x= (c*e-f*b)/(a*e-d*b)
    y= (f-d*x)/e
print(int(x), int(y))