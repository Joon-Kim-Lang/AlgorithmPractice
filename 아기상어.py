N = int(input())
from collections import deque

mapList = [[-1] * (N+2) for _ in range(N+2)]

sharkRow = 0
sharkCol = 0
for i in range(1, N+1):
  tempList = list(map(int, input().split()))
  for j in range(1, N+1):
    mapList[i][j] = tempList[j-1]
    if tempList[j-1] == 9:
      sharkRow , sharkCol = i ,j
      mapList[i][j] = 0

isPreyLeft = True
sharkSize = 2
curCnt = 0
result = 0
while isPreyLeft:
  caughtList = []
  isVisited =[[False] * (N+2) for _ in range(N+2)]
  qu = deque()
  qu.append((sharkRow, sharkCol,0))
  isVisited[sharkRow][sharkCol] = True

  while qu:   
    i, j, curDepth = qu.popleft()
    if isVisited[i-1][j] == False:
      if mapList[i-1][j] == -1 or mapList[i-1][j] > sharkSize:
        isVisited[i-1][j] = True
      elif 0< mapList[i-1][j] < sharkSize:
        isVisited[i-1][j] = True
        caughtList.append( ( curDepth+1, i-1, j ))
        qu.append((i-1,j,curDepth+1))
      elif mapList[i-1][j] == sharkSize or  mapList[i-1][j] ==0:
        isVisited[i-1][j] = True
        qu.append((i-1,j,curDepth+1))
    #남쪽탐사
    if isVisited[i+1][j] == False:
      if mapList[i+1][j] == -1 or mapList[i+1][j] > sharkSize:
        isVisited[i+1][j] = True
      elif 0< mapList[i+1][j] < sharkSize:
        isVisited[i+1][j] = True
        caughtList.append( ( curDepth+1, i+1, j ))
        qu.append((i+1,j,curDepth+1))
      elif mapList[i+1][j] == sharkSize or mapList[i+1][j] ==0:
        isVisited[i+1][j] = True
        qu.append((i+1,j,curDepth+1))
    #서쪽탐사
    if isVisited[i][j-1] == False:
      if mapList[i][j-1] == -1 or mapList[i][j-1] > sharkSize:
        isVisited[i][j-1] = True
      elif 0< mapList[i][j-1] < sharkSize:
        isVisited[i][j-1] = True
        caughtList.append( ( curDepth+1, i, j-1 ))
        qu.append((i,j-1,curDepth+1))
      elif mapList[i][j-1] == sharkSize or mapList[i][j-1] ==0:
        isVisited[i][j-1] = True
        qu.append((i,j-1,curDepth+1))
    #동쪽탐사
    if isVisited[i][j+1] == False:
      if mapList[i][j+1] == -1 or mapList[i][j+1] > sharkSize:
        isVisited[i][j+1] = True
      elif 0< mapList[i][j+1] < sharkSize:
        isVisited[i][j+1] = True
        caughtList.append( ( curDepth+1, i, j+1 ))
        qu.append((i,j+1,curDepth+1))
      elif mapList[i][j+1] == sharkSize or mapList[i][j+1] == 0:
        isVisited[i][j+1] = True
        qu.append((i,j+1,curDepth+1))

  if len(caughtList) == 0:
    isPreyLeft = False
    break
  else:
    caughtList = sorted(caughtList, key= lambda x : (x[0], x[1], x[2]) )
    curCnt+=1
    sharkRow = caughtList[0][1]
    sharkCol = caughtList[0][2]
    result +=  caughtList[0][0]
    mapList[sharkRow][sharkCol] = 0
    if curCnt == sharkSize:
      curCnt = 0
      sharkSize +=1

print(result)