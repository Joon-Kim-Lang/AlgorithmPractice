import heapq

N, M, dist, start = map(int,input().split())
connectInfo  = [[] for _ in range(N+1)]

for _ in range(M):
  fr, to = map(int, input().split())
  connectInfo[fr].append(to)

INF = int(1e9)

distance = [INF] *(N+1)

qu = []

distance[start] = 0
heapq.heappush(qu, (0, start))

while qu:
  curDist, curNum = heapq.heappop(qu)
  if distance[curNum] < curDist:
    continue
  
  for next in connectInfo[curNum]:
    cost = curDist + 1
    if cost < distance[next]:
      distance[next] = cost
      heapq.heappush(qu, (cost, next))

isFound =False
for i, v in enumerate(distance):
  if v == dist:
    print(i)
    isFound = True
if isFound ==False:
  print(-1)

