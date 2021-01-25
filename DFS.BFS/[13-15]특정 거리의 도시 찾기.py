import heapq

nodeNum,edgeNum,targetDist,startNode = map(int, input().split())

#노드 간 연결정보입력
nodeList = {}

for i in range(nodeNum):
  nodeList[i+1] = {}

for i in range(edgeNum):
  start, end = map(int, input().split())
  nodeList[start][end] = 1

#다익스트라 구현
def dijkstra(startNode, nodeList):
  opt_dist_list = {node : float('inf') for node in nodeList}
  opt_dist_list[startNode] = 0

  heap = []

  heapq.heappush(heap, [opt_dist_list[startNode], startNode])

  while heap:
    distance, curNode = heapq.heappop(heap)

    if opt_dist_list[curNode] < distance:
      continue

    for arrival, distance2 in nodeList[curNode].items():
      opt_distance = distance + distance2

      if(opt_distance < opt_dist_list[arrival]):
        opt_dist_list[arrival] = opt_distance
        heapq.heappush(heap, [opt_dist_list[arrival], arrival])

  return opt_dist_list

result = dijkstra(startNode,nodeList)

checkIsnull = True
for i in nodeList:
  if result[i] == targetDist:
    print(i)
    checkIsnull = False

if checkIsnull:
  print(-1) 



