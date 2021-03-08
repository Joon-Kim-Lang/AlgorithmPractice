N = int(input())
from collections import deque

mapList = []
for i in range(N+2):
  mapList.append([])
  for j in range(N+2):
    if i == 0 or i == N+1 or j == 0 or j == N+1:
      mapList[i].append(7)
    else:
      mapList[i].append(0)

directions = {'N':(-1,0), 'S':(1,0),'E':(0,1),'W':(0,-1)}
dirQu = deque()

#사과 개수
M = int(input())

for _ in range(M):
  row, col = map(int, input().split())
  mapList[row][col] = 2

#방향전환정보
K = int(input())

for _ in range(K):
  sec, direction = input().split()
  dirQu.append((int(sec), direction))

#시작 전 초기화
mapList[1][1] = 1
curDir = 'E'
snakeQu = deque()
snakeQu.append((1,1))

result = 0

while True:
  # #맵 출력
  # for i in range(N+2):
  #   for j in range(N+2):
  #     print(mapList[i][j], end=' ')
  #   print()
  # print()

  curHead = snakeQu[0]
  newRow, newCol = curHead[0] + directions[curDir][0], curHead[1] + directions[curDir][1]
  if mapList[newRow][newCol] == 7 or mapList[newRow][newCol] == 1:
    print(result +1)
    break

  elif mapList[newRow][newCol] == 0:
    mapList[newRow][newCol] = 1
    snakeQu.appendleft((newRow, newCol))
    deleteInfo = snakeQu.pop()
    mapList[deleteInfo[0]][deleteInfo[1]] = 0
  #사과 있을 경우
  elif mapList[newRow][newCol] == 2:
    mapList[newRow][newCol] = 1
    snakeQu.appendleft((newRow, newCol))

  result+=1

  if len(dirQu) > 0:
    if dirQu[0][0] == result:
      curDirInfo = dirQu.popleft()
      if curDirInfo[1] == 'D':
        if curDir == 'E': curDir = 'S'
        elif curDir == 'S': curDir = 'W'
        elif curDir == 'W' : curDir = 'N'
        else : curDir = 'E'
      else:
        if curDir == 'E': curDir = 'N'
        elif curDir == 'S': curDir = 'E'
        elif curDir == 'W' : curDir = 'S'
        else : curDir = 'W'