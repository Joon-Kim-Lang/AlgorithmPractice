from collections import deque
import sys

T = int(sys.stdin.readline().rstrip())

directions = [(1,0), (-1,0),(0,1),(0,-1)]

def UpdateFire(mapList, fireQu,fireVisited):
  newQu = deque()

  while fireQu:
    curR, curC = fireQu.popleft()   
    
    for direction in directions:
      newR = curR + direction[0]
      newC = curC + direction[1]

      if mapList[newR][newC] == '.' and fireVisited[newR][newC] == False:
        mapList[newR][newC] = '*'
        fireVisited[newR][newC] = True
        newQu.append((newR,newC))
  
  return newQu

resultList = []

#테스트 케이습 반복
for _ in range(T):

  W, H = map(int,sys.stdin.readline().split())

  mapList = [[-1] * (W+2) for _ in range(H+2)]
  
  stR, stC = 0, 0
  
  fireVisited = [[False] * (W+2) for _ in range(H+2)]
  manVisited = [[False] * (W+2) for _ in range(H+2)]
  fireQu = deque()

  for h in range(1, H+1):
    tempStr = sys.stdin.readline().rstrip()
    for w in range(1, W+1):  
      mapList[h][w] = tempStr[w-1]
      if tempStr[w-1] == '@':
        stR, stC = h, w
        mapList[h][w] = '.'
      elif tempStr[w-1] == '*':
        fireQu.append((h, w))
        fireVisited[h][w] = True

  manQu = deque()
  manQu.append((stR,stC,0))
  flag = -1
  result = []

  while manQu:

    curH, curC , curT = manQu.popleft()
    #불정보 업데이트
    if curT != flag:
      fireQu = UpdateFire(mapList, fireQu, fireVisited)
      flag += 1
    
    for direction in  directions:
      newH = direction[0] + curH
      newC = direction[1] + curC
      if mapList[newH][newC] == '.'and manVisited[newH][newC] == False:
        manQu.append((newH,newC, curT+1))
        manVisited[newH][newC] = True
      elif mapList[newH][newC] == -1 and manVisited[newH][newC] == False:
        result.append(curT+1)
        break
  
  if len(result) == 0:
    resultList.append("IMPOSSIBLE")
  else:
    resultList.append(result[0])

for i in resultList:
  print(i)