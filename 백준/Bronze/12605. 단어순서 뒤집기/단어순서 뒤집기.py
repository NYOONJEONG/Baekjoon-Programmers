n = int(input())
cnt = 0
for i in range(n):
    text = input().split()
    print(f"Case #{i+1}: {' '.join(text[::-1])}")