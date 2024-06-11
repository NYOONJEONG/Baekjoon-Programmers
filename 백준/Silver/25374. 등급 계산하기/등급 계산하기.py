n = int(input())
score= list(map(int, input().split()))
grade = [100, 96, 89, 77, 60, 40, 23, 11, 4]
score.sort()
cnt = 0
counted= 0
idx = 8
i = n-1
while i>-1:
    cur = score[i]
    while i > -1 and score[i]==cur:
        cnt += 1
        i -= 1
    while idx > -1 and n*grade[idx] <= 100 * cnt:
        print(cnt-counted)
        counted = cnt
        idx -= 1