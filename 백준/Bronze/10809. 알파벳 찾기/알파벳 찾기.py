S = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in list(alphabet):
    if i in list(S) :
        print(S.index(i), end= ' ')
    else : print(-1, end=' ')