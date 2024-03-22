def solution(friends, gifts):
    answer = 0
    n = len(friends)
    give = [[0] * n for _ in range(n)]
    score = [0] * n
    
    for gift in gifts:
        gift = gift.split()
        a = friends.index(gift[0])
        b = friends.index(gift[1])
        
        give[a][b] += 1
        
    for i in range(n):
        for j in range(i+1,n):
            give_score = give[i][j] # i가 j에게 준 선물의 개수
            get_score = give[j][i] #j가 i에게 준 선물의 개수
            
            # 서로 주고 받은 경우
            if (give_score != get_score) and (give_score>0 or get_score>0):
                if give_score > get_score:    
                    score[i] += 1
                else : 
                    score[j] += 1
            else : # 주고 받은 개수가 같거나/ 받거나 준게 없으면
                giver_total_score = sum(give[i])
                getter_total_score = sum(give[j])
                
                for k in range(n):
                    giver_total_score -= give[k][i]
                    getter_total_score -= give[k][j]
                
                if giver_total_score > getter_total_score :
                    score[i] += 1
                    
                elif giver_total_score < getter_total_score:
                    score[j] += 1
                else : pass
                
    answer = max(score)
    return answer