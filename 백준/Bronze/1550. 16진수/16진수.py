n= list(input())
m = len(n)
def change(x):
    if x =='1':
        x= 1
    elif x=='2':
        x=2
    elif x=='3':
        x=3
    elif x=='4':
        x=4
    elif x=='5':
        x=5
    elif x=='6':
        x=6
    elif x=='7':
        x=7
    elif x=='8':
        x=8
    elif x=='9':
        x=9
    elif x=='A':
        x=10
    elif x=='B':
        x=11
    elif x=='C':
        x=12
    elif x=='D':
        x=13
    elif x=='E':
        x=14
    elif x=='F' :
        x=15
    else : 
        x= 0
    return x
output = 0
for i in range(m):
    x = change(n[m-i-1])
    output += x * 16**i

print(output)