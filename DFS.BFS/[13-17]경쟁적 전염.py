import heapq

N, K = map(int, input().split())

mapList = []

for i in range(N+2):
  mapList.append([])
  for j in range(N+2):
    mapList[i].append(-1)

for i in range(1, N+1):
  tempList = list(map(int, input().split()))
  for j in range(1, N+1):
    mapList[i][j] = tempList[j-1]

S, X, Y = map(int, input().split())

#[종류,행,열]
heap = []

#초기 상황 초기화
for i in range(1, N+1):
  for j in range(1, N+1):
    if mapList[i][j] > 0:
      heapq.heappush(heap, [mapList[i][j], i,j])

#알고리즘 시작
curTime = 0

while curTime < S:
  newHeap = []
  while heap:
    tempEle = heapq.heappop(heap)
    #사방이 막혔으면 컨티뉴
    if mapList[tempEle[1]-1][tempEle[2]] !=0 and mapList[tempEle[1]+1][tempEle[2]] !=0 and mapList[tempEle[1]][tempEle[2]-1] !=0 and mapList[tempEle[1]][tempEle[2]+1] !=0:
      continue

    if mapList[tempEle[1]-1][tempEle[2]] == 0:
      mapList[tempEle[1]-1][tempEle[2]] = tempEle[0]
      heapq.heappush(newHeap, [tempEle[0], tempEle[1]-1,tempEle[2]])
    if mapList[tempEle[1]+1][tempEle[2]] == 0:
      mapList[tempEle[1]+1][tempEle[2]] = tempEle[0]
      heapq.heappush(newHeap, [tempEle[0], tempEle[1]+1,tempEle[2]])
    if mapList[tempEle[1]][tempEle[2]-1] == 0:
      mapList[tempEle[1]][tempEle[2]-1] = tempEle[0]
      heapq.heappush(newHeap, [tempEle[0], tempEle[1],tempEle[2]-1]) 
    if mapList[tempEle[1]][tempEle[2]+1] == 0:
      mapList[tempEle[1]][tempEle[2]+1] = tempEle[0]
      heapq.heappush(newHeap, [tempEle[0], tempEle[1],tempEle[2]+1])

    heapq.heappush(newHeap, [tempEle[0], tempEle[1], tempEle[2]]) 

  curTime +=1
  heap = newHeap

print(mapList[X][Y])  
