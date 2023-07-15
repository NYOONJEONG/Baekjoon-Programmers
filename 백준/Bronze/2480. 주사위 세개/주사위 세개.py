a,b,c = map(int, input().split())

if a==b==c:
    award = 10000+ a * 1000
elif a==b and b!=c:
    award = 1000 + a * 100
elif b==c and b!=a :
    award = 1000 + b * 100
elif a==c and a!=b:
    award = 1000 + c* 100
else :
    award = max(a,b,c) * 100

print(award)