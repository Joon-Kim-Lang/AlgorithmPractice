import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e, start = map(int,input().split())
mapList = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for i in range(e):
  f, t, c = map(int, input().split())
  mapList[f].append((t,c))

def dijkstra(start):
  qu  = []
  distance[start] = 0
  heapq.heappush(qu, (0, start))

  while qu:
    cost, curNode = heapq.heappop(qu)

    if distance[curNode] < cost:
      continue
    
    for i in mapList[curNode]:
      newCost = cost + i[1]
      if newCost < distance[i[0]]:
        distance[i[0]] = newCost
        heapq.heappush(qu, (newCost,i[0]))

dijkstra(start)
totalcity = 0
totalcost = 0
for i in range(1, v+1):
  if distance[i] != INF:
    totalcity +=1
    totalcost = max(totalcost, distance[i])

print(totalcity -1, totalcost)

