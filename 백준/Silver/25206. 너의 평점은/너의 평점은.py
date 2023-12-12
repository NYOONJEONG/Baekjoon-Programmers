total = 0
cumsum = 0
for _ in range(20):
    subject, score, grade = input().split()
    score = float(score)
    if grade=='A+' :
        total += score
        cumsum += score * 4.5
    elif grade =="A0":
        total += score
        cumsum += score*4.0
    elif grade == "B+":
        total += score
        cumsum += score* 3.5
    elif grade == "B0":
        total += score
        cumsum += score * 3
    elif grade == "C+":
        total += score
        cumsum += score* 2.5
    elif grade == "C0":
        total += score
        cumsum += score * 2.0
    elif grade == "D+":
        total += score
        cumsum += score* 1.5
    elif grade == "D0":
        total += score
        cumsum += score * 1.0
    elif grade == "F":
        total += score
        cumsum += score * 0
    else : pass
print(cumsum/total)