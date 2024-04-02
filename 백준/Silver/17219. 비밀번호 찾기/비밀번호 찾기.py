n, m = map(int, input().split())
dict= {}
for _ in range(n):
    www, pwd = input().split()
    dict[www] = pwd
for _ in range(m):
    find = input()
    print(dict[find])