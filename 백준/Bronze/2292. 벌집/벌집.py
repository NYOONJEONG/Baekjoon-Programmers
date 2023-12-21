N = int(input())
row = 1  
output= 1
while N  > row :
    row += 6 * output
    output += 1
print(output)