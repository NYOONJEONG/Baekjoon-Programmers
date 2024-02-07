N = int(input())
road = list(map(int, input().split()))
station = list(map(int, input().split()))
cost = 0
for i in range(N-1):
    if station[i]==min(station[i:N-1]) :
        cost += station[i] * sum(road[i:N-1]) 
        break
    else: cost += station[i] * road[i]

print(cost)