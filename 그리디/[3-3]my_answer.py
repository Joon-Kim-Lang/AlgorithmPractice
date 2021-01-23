n, m = map(int, input().split())

maxNum = 0

for i in range(n):
    data = list(map(int, input().split()))
    listMin = min(data)
    if listMin > maxNum:
        maxNum = listMin
        
print(maxNum)
