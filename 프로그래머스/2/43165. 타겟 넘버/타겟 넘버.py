from collections import deque

def solution(numbers, target):
    def bfs(numbers, target):
        global answer
        answer = 0
        queue = deque()
        queue.append((-numbers[0],0)) # 숫자, 인덱스
        queue.append((numbers[0],0))
        while queue:
            num, idx = queue.popleft()
            if idx < len(numbers)-1:
                idx += 1
                queue.append((num + numbers[idx],idx))
                queue.append((num- numbers[idx], idx))
            else : 
                if num == target: 
                    answer += 1
    bfs(numbers, target)        
    return answer