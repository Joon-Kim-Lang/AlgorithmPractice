import heapq

N = int(input())

qu = []
operList = []
for _ in range(N):
  operList.append(int(input()))

for oper in operList:
  if oper == 0:
    if len(qu) > 0:
      print(qu[0])
      heapq.heappop(qu)
    else:
      print(0)
  else:
    heapq.heappush(qu, oper)