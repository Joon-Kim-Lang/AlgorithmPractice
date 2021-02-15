import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append((b,1))
  graph[b].append((a,1))

#다익스트라 시작

qu = []
distance[1] = 0
heapq.heappush(qu, (0,1))

while qu:
  cost, curNode = heapq.heappop(qu)
   
  if cost > distance[curNode]:
    continue
  
  for v in graph[curNode]:
    newCost = cost + v[1]
    if newCost < distance[v[0]]:
      distance[v[0]] = newCost
      heapq.heappush(qu, (newCost, v[0]))

longestCase = -1
longestIdx = 0
for i in range(2, N+1):
  if distance[i] > longestCase:
    longestCase = distance[i]
    longestIdx = i

sameCnt = distance[2:].count(longestCase)

print(longestIdx,longestCase,sameCnt)   