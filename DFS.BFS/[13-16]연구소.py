from itertools import combinations
import copy
from collections import deque

R, C = map(int, input().split())

mapList= []
for i in range(R+2):
  mapList.append([])
  for j in range(C+2):
    mapList[i].append(1)

for i in range(1, R+1):
  tempList = list(map(int, input().split()))
  for j in range(1, C+1):
    mapList[i][j] = tempList[j-1]

#빈 공간 콤비네이션 조합 구하기
vacancyList = []
for i in range(1, R+1):
  for j in range(1, C+1):
    if mapList[i][j] == 0:
      vacancyList.append([i,j])

vacancyComb = list(combinations(vacancyList,3))

def plagueSim(mapList, R, C):
  mapList = copy.deepcopy(mapList)
  safeArea = 0
  tempList = deque()

  for i in range(1, R+1):
    for j in range(1, C+1):      
      if mapList[i][j] == 2:
        tempList.append([i,j])
        while len(tempList) > 0:
          curIdx = tempList.popleft()
          if mapList[curIdx[0]-1][curIdx[1]] == 0:
             mapList[curIdx[0]-1][curIdx[1]] = 2
             tempList.append([curIdx[0]-1, curIdx[1]])
          if mapList[curIdx[0]+1][curIdx[1]] == 0:
             mapList[curIdx[0]+1][curIdx[1]] = 2
             tempList.append([curIdx[0]+1, curIdx[1]])
          if mapList[curIdx[0]][curIdx[1]-1] == 0:
             mapList[curIdx[0]][curIdx[1]-1] = 2
             tempList.append([curIdx[0], curIdx[1]-1])
          if mapList[curIdx[0]][curIdx[1]+1] == 0:
             mapList[curIdx[0]][curIdx[1]+1] = 2
             tempList.append([curIdx[0], curIdx[1]+1])

  for i in range(1, R+1):
    for j in range(1, C+1):
      if mapList[i][j] == 0:
        safeArea +=1

  return safeArea

maxSafeArea = 0

for i in vacancyComb:
  for j in range(3):
    mapList[i[j][0]][i[j][1]] = 1

  tempSafeArea = plagueSim(mapList, R, C)

  maxSafeArea = max(maxSafeArea,tempSafeArea)

  for j in range(3):
    mapList[i[j][0]][i[j][1]] = 0

print(maxSafeArea)