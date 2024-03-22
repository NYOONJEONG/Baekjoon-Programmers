import heapq
def calculate(a,b):
    return a+2*b

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    
    while len(scoville)>=2 and scoville[0] < K:
        a= heapq.heappop(scoville)
        b= heapq.heappop(scoville)
        x = calculate(a,b)
        heapq.heappush(scoville, x)
        cnt += 1
    
    if len(scoville)==1 and scoville[0]<K : # 안될때(무조건 하나 남을 때)
        return -1
    
    return cnt