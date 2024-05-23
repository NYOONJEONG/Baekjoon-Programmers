from itertools import permutations
def solution(k, dungeons):
    answer = -1
    possible = list(permutations(dungeons,len(dungeons)))  
    for lst in possible:
        k_lst = k
        cnt= 0
        for l in lst:
            minimum, usage = l[0],l[1]
            if k_lst>=minimum:
                k_lst -= usage
                cnt +=1
            else: 
                break
        answer= max(cnt, answer)
    return answer