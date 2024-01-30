N = int(input())
num = sorted(map(int, input().split()))
M = int(input())
have = list(map(int,input().split()))

def search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2

        if array[mid] == target :
            return num[start:end+1].count(target)
        elif array[mid] > target :
            end = mid-1
        else: 
            start = mid +1
    return None

count = {}
for x in num:
    start = 0
    end = len(num) - 1
    if x not in count:
        count[x] = search(num, x, start, end)

print(' '.join(str(count[x]) if x in count else '0' for x in have))