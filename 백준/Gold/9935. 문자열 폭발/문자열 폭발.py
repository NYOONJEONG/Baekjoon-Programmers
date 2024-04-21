import sys
input = sys.stdin.readline

text = list(input().strip())
bomb = list(input().strip())

output = []
for x in text :
    output.append(x)
    if output[-len(bomb)::]== bomb :
          del output[-len(bomb):]
if output == [] : 
      print("FRULA")
else : 
    for x in output:
            print(x, end="")