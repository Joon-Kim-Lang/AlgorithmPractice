N = int(input())

distList = list(map(int, input().split()))
opList = list(map(int, input().split()))

curMinPrice = 1000000001

result = 0

for i in range(len(opList)-1):
  curMinPrice = min(curMinPrice, opList[i])
  result += (curMinPrice*distList[i])

print(result)