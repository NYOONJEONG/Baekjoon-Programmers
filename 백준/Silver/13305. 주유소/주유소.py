N = int(input())
road = list(map(int, input().split()))
station = list(map(int, input().split()))
cost = 0
min_station = station[0]

for i in range(N-1):
    if station[i] < min_station :
        min_station = station[i]
    cost += min_station * road[i]
print(cost)