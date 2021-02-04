N = int(input())
storeList = list(map(int, input().split() ))
M = int(input())
orderList = list(map(int, input().split()))

for i in orderList:
  if i in storeList:
    print("yes", end= ' ')
  else:
    print("no", end = ' ')