import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

if m!=0:
    wrong = set(map(int, input().split()))
else : 
    wrong = []

cnt = abs(100-n)

maximum = 1000000
for x in range(maximum) : # x는 고장나지 않은 버튼만으로 
    for i in str(x):
        if int(i) in wrong:
            break
    else : 
        cnt = min(cnt, len(str(x)) + abs(x-n)) 
        #  len(str(x)) : 숫자 누르고
        # abs(x-n): 더하거나/빼서 이동
print(cnt)