M, N = map(int, input().split()) #M행 N렬
block = []
block = []
result = []
for i in range(M):
    block.append(input())
result = []
for i in range(M-7):
    for j in range(N-7):
        white = 0
        black = 0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2 == 0 :
                    if block[a][b] != "W":
                        white += 1
                    if block[a][b] != "B":
                        black += 1
                else: 
                    if block[a][b] != "B":
                        white += 1
                    if block[a][b] != "W":
                        black += 1
        result.append(white)
        result.append(black)
                    
print(min(result))