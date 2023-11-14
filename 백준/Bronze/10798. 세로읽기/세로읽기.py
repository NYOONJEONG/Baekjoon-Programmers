words = [input() for i in range(5)]
for j in range(15):
    for k in range(5):
        if j < len(words[k]):
            print(words[k][j], end='')