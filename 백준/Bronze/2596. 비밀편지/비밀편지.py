solve = {
  '000000' : 'A',
  '001111' : 'B',
  '010011' : 'C',
  '011100' : 'D',
  '100110' : 'E',
  '101001' : 'F',
  '110101' : 'G',
  '111010' : 'H'
}
n = int(input())
code = input()

answer = ""
for i in range(n):
    cut = code[6*i: 6*(i+1)]
    if solve.get(cut):
        answer += solve[cut]
    else:
        tmp = ""
        for x in solve.keys():
            check = bin((int(x,2)^int(cut,2)))
            if check.count("1")==1:
                tmp= solve[x]
        
        if tmp :
            answer += tmp
        else :
            print(i+1)
            break
if len(answer)==n:
    print(answer)