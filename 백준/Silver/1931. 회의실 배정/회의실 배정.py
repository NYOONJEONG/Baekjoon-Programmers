import sys
timeline =[]
N =int(sys.stdin.readline())
for i in range(N):
    timeline.append(list(map(int, sys.stdin.readline().split())))
timeline.sort(key=lambda x : (x[1], x[0]))

end =0
output = 0

for newstart, newend in timeline:
    if end <= newstart :
        output += 1
        end = newend
print(output)