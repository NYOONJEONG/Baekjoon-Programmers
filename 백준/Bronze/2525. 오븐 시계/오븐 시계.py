H, M = map(int, input().split())
x = int(input())

if M+x<60 : 
    hour = H
    minute = M+x
elif M+x>=60 and (H + (M+x)//60)<24 :
    hour = H + (M+x)//60
    minute = (M+x)%60
else : 
    hour = H + (M+x)//60 -24
    minute = (M+x)%60
print(hour, minute)
    