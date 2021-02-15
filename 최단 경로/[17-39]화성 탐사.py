import heapq
import sys
input = sys.stdin.readline

T = int(input())
INF = int(1e9)
resultList = []

#테스트케이스 루프
for _ in range(T):
  N = int(input())
  #지도 생성
  mapList = [[-1]* (N+2) for _ in range(N+2) ]
  
  for r in range(1, N+1):
    tempInput = list(map(int, input().split()))
    for c in range(1, N+1):
      mapList[r][c] = tempInput[c-1]

  distance = [INF] * (N*N + 1)
  graph = [[] for i in range(N*N + 1)]

  curIdx = 1
  for r in range(1, N+1):
    for c in range(1, N+1):
      #상하좌우 확인
      if mapList[r-1][c] != -1:
        graph[curIdx].append((curIdx-N, mapList[r-1][c]))
      if mapList[r+1][c] != -1:
        graph[curIdx].append((curIdx+N, mapList[r+1][c]))
      if mapList[r][c-1] != -1:
        graph[curIdx].append((curIdx-1, mapList[r][c-1]))
      if mapList[r][c+1] != -1:
        graph[curIdx].append((curIdx+1, mapList[r][c+1]))

      curIdx+=1

  #다익스트라 적용
  qu =  []
  distance[1] = 0
  heapq.heappush(qu, (0,1))

  while qu:
    cost, curNode = heapq.heappop(qu)
    if cost > distance[curNode]:
      continue
    else:
      for i in graph[curNode]:
        newCost = cost + i[1]
        if newCost < distance[i[0]]:
          distance[i[0]] = newCost
          heapq.heappush(qu, (newCost, i[0]))

  #마지막에 처음 첫 위치 비용 넣을 것
  resultList.append(distance[N*N] + mapList[1][1])

for i in resultList:
  print(i)