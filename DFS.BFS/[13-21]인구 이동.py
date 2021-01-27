N, L, R = map(int, input().split())
from collections import deque
import copy

popList = []
isVisited = []
for i in range(N+2):
  popList.append([])
  isVisited.append([])
  for j in range(N+2):
    popList[i].append(float("inf"))
    isVisited[i].append(False)

corList=[]
for i in range(1,N+1):
  tempInput = list(map(int, input().split()))
  for j in range(1,N+1):
    popList[i][j] = tempInput[j-1]
    corList.append([i,j])

#인구이동 발생조건--> 연합 X
moveCnt = 0
while True:
  tempVisited = copy.deepcopy(isVisited)
  curUtdList = []
  curSumList = []
#연합 형성
  for i in range(1, N+1):
    for j in range(1, N+1):
      if tempVisited[i][j] == False:
        curUtdEle = []
        tempQu = deque()
        tempQu.append([i,j])
        tempVisited[i][j] = True
        tempSum = 0
        while tempQu:      
          curState = tempQu.popleft()
          curUtdEle.append(curState)
          tempSum += popList[curState[0]][curState[1]]
          #위쪽검사
          if L <= abs(popList[curState[0]][curState[1]] - popList[curState[0]-1][curState[1]]) <=R and tempVisited[curState[0]-1][curState[1]] == False:
            tempQu.append([curState[0]-1, curState[1]])
            tempVisited[curState[0]-1][curState[1]] = True
          #아래쪽검사
          if L <= abs(popList[curState[0]][curState[1]] - popList[curState[0]+1][curState[1]]) <=R and tempVisited[curState[0]+1][curState[1]] == False:
            tempQu.append([curState[0]+1, curState[1]])
            tempVisited[curState[0]+1][curState[1]] = True
          #왼쪽검사
          if L <= abs(popList[curState[0]][curState[1]] - popList[curState[0]][curState[1]-1]) <=R and tempVisited[curState[0]][curState[1]-1] == False:
            tempQu.append([curState[0], curState[1]-1])
            tempVisited[curState[0]][curState[1]-1] = True
          #오른쪽검사
          if L <= abs(popList[curState[0]][curState[1]] - popList[curState[0]][curState[1]+1]) <=R and tempVisited[curState[0]][curState[1]+1] == False:
            tempQu.append([curState[0], curState[1]+1])
            tempVisited[curState[0]][curState[1]+1] = True
        
        if len(curUtdEle) > 1:
          curUtdList.append(curUtdEle)
          curSumList.append(tempSum)

  #인구이동발생
  if len(curUtdList) == 0:
    break
  else:
    moveCnt +=1
    lenCnt = 0
    for i in curUtdList:
      for j in i:
        popList[j[0]][j[1]] = curSumList[lenCnt] // len(i)
      lenCnt+=1

print(moveCnt)