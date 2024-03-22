def find(n, k):
    if n==None:
        return [k, -k]
    return [n-k, n+k, n//k, n*k]

def solution(N, number):
    if N==number:
        return 1

    dp = []
    dp.append([None])
    dp.append([N,-N])
    for i in range(1,8):
        temp = []
        
        for x in dp[i]:
            temp.extend(find(x, N))

        prod = 11
        for j in range(i):
            for element in dp[i-j-1]:
                temp.extend(find(element, N*prod))
            prod += 10 ** (j+2)
        
        if number in temp:
            return i+1 # 최소값 출력
        dp.append(temp)
        
    return -1