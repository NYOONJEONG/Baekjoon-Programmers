equation = input().split("-")
calculate =[]

for x in equation:
    num = []
    dummy=0
    num = map(int, x.split("+"))
    for y in num :
        dummy += y
    calculate.append(dummy)
    
output = calculate[0]
for i in range(1, len(calculate)):
    output -= calculate[i]
print(output)