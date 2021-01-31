import heapq

N = int(input())

numList = []
for i in range(N):
  heapq.heappush(numList, int(input()))

totComp = 0


while len(numList) > 1:
  first = heapq.heappop(numList)
  second = heapq.heappop(numList)
  newEle = first + second
  totComp = totComp + newEle
  heapq.heappush(numList, newEle)

print(totComp)