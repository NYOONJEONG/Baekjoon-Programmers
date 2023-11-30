x, y, w, h = map(int, input().split())
distance = [x, y, abs(x-w), abs(y-h), ((x-w)**2+(y-h)**2)**(1/2)]
print(min(distance))