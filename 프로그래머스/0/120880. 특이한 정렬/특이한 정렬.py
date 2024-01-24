def solution(numlist, n):
    answer = []
    dist = []
    for i in numlist:
        dist.append(i)
        dist.sort(key=lambda x : (abs(x-n), -x))
    return dist