def find(want, number, product):
    if product in want: 
        for i in range(len(want)):
            if want[i]== product and number[i]>0:
                number[i]-=1
                break
    return number

def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        find_num = number.copy()
        for j in range(10):
            find_num = find(want, find_num, discount[i+j])
        if find_num==[0 for i in range(len(want))] :
            answer+=1
    if answer==0:
        return 0
    else: 
        return answer