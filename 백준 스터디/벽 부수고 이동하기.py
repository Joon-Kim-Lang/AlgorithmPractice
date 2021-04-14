from collections import deque
import sys

N, M = map(int,sys.stdin.readline().split())

directions = [(-1,0), (1,0),(0,-1),(0,1)]

mapList = []

for n in range(N+2):
  mapList.append([])
  for m in range(M+2):
    mapList[n].append(-1)

isVisited = [[[0]*2 for _ in range(M+2)] for _ in range(N+2)]

#입력에 따른 맵 정보 갱신
for n in range(1,N+1):
  tempStr = sys.stdin.readline().strip()
  for m in range(1,M+1):
    mapList[n][m] = int(tempStr[m-1])

qu = deque()
qu.append((1,1,0))

result = []

while qu:  

  row, col, isbreaked = qu.popleft()

  if row == N and col == M:
    result.append((row,col,isbreaked))
    break

  for direction in directions:
    newRow = direction[0] + row
    newCol = direction[1] + col

    if mapList[newRow][newCol] == 1 and isbreaked == 0:
      qu.append((newRow, newCol, 1))
      isVisited[newRow][newCol][1] = isVisited[row][col][isbreaked] + 1  

    elif mapList[newRow][newCol] == 0 and isVisited[newRow][newCol][isbreaked] == 0 :
      qu.append((newRow, newCol, isbreaked))
      isVisited[newRow][newCol][isbreaked] = isVisited[row][col][isbreaked] + 1
      if isbreaked == 0:
        isVisited[newRow][newCol][1] = isVisited[newRow][newCol][0]



if len(result) == 0:
  print(-1)
else:
  r, c, w = result[0]
  print(isVisited[r][c][w] +1)