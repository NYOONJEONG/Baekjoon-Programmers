N = int(input())
count = 0 
for i in range(N):
    text = input()
    for j in range(1,len(text)):
        if (text[j]!=text[j-1]) & (text[j] in text[:j]) : 
                count +=1 
                break
print(N-count)