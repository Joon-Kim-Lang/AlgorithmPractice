import copy
from collections import deque

directions = [(),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
mapList= [[[-1,0]]*6 for _ in range(6)]

#초기 맵 정보 생성
for i in range(1,5):
  tempList = list(map(int, input().split()))
  for j in range(len(tempList)):
    if j % 2 == 0:
      idxJ = j // 2
      mapList[i][idxJ+1] = [tempList[j], tempList[j+1]]

result = 0
mapQu = deque()
startMap = copy.deepcopy(mapList)
startMap[1][1][0] = 'S'
mapQu.append(startMap)


while mapQu:
  curMapList = mapQu.popleft()

  #물고기 움직임
  for i in range(1, 17):
    loopFlag = False
    for row in range(1,5):
      if loopFlag: break
      for col in range(1,5):
        #현재 상어의 위치 파악
        if curMapList[row][col][0] == 'S':
          sRow, sCol, sDir = row, col, curMapList[row][col][1]
        #현재 번호의 물고기의 위치 갱신
        if curMapList[row][col][0] == i:
          tempDir = curMapList[row][col][1]
          while True:
            if (curMapList[row+directions[tempDir][0]][col+directions[tempDir][1]][0] == -1) or (curMapList[row+directions[tempDir][0]][col+directions[tempDir][1]][0] == 'S'):
              tempDir +=1
              if tempDir == 9:
                tempDir = 1
              
            else:
              curMapList[row][col][1] = tempDir
              curMapList[row+directions[tempDir][0]][col+directions[tempDir][1]], curMapList[row][col] = curMapList[row][col], curMapList[row+directions[tempDir][0]][col+directions[tempDir][1]]
              loopFlag = True
              break

            if tempDir == curMapList[row][col][1]:
              loopFlag = True
              break

          if loopFlag: break
  
  endFlag = True
  #상어 움직임(먹을 경우 원래 상어 위치를 0으로 갱신해주어야함)) + 먹을 경우 endflag 갱신
  sOriRow = sRow
  sOriCol = sCol
  while curMapList[sRow + directions[sDir][0]][sCol + directions[sDir][1]][0] != -1:
    goalPos = curMapList[sRow + directions[sDir][0]][sCol + directions[sDir][1]]
    if str(goalPos[0]).isnumeric():
      if 1 <=  goalPos[0]:
        tempMap = copy.deepcopy(curMapList)
        tempMap[sOriRow][sOriCol] = [0,0]
        tempMap[sRow + directions[sDir][0]][sCol + directions[sDir][1]][0] = 'S'
        mapQu.append(tempMap)
        endFlag = False
    sRow,sCol = sRow + directions[sDir][0], sCol + directions[sDir][1]
              
  if endFlag:
    tempResult = int(16*17/2)
    for i in range(1, 17):
      for row in range(1,5):
        for col in range(1,5):
          if curMapList[row][col][0] == i:
            tempResult -= i
    
    if tempResult > result:
      result = tempResult

print(result)