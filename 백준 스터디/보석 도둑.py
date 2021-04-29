import heapq
import sys

N, K  = map(int, sys.stdin.readline().split())

jewelList = []
bag = []
jewelQu = []

for _ in range(N):
  w, v = map(int, sys.stdin.readline().split())
  jewelList.append((w,v))

jewelList = sorted(jewelList, key = lambda x : x[0])

for _ in range(K):
  bag.append( int(sys.stdin.readline()))

bag.sort()

answer = 0
idx = 0

for b in bag:
  while idx < N and jewelList[idx][0] <= b:
    heapq.heappush(jewelQu, -jewelList[idx][1])
    idx +=1
  
  if jewelQu:
    answer -= heapq.heappop(jewelQu)

print(answer)