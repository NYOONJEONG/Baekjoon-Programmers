def solution(ineq, eq, n, m):
    answer = 0
    if (ineq == "<") & (eq=="="):
        if n<=m : answer =1
        else : answer = 0
    elif (ineq=="<")&(eq=="!"):
        if n<m : answer =1
        else : answer =0
    elif (ineq==">")&(eq=="="):
        if n>=m : answer= 1
        else : answer =0
    else : 
        if n>m : answer=1
        else : answer=0
    return answer