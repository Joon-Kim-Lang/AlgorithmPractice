from collections import deque
import sys

M,N,H = map(int, sys.stdin.readline().split())
mapList = []
for h in range(H+2):
  mapList.append([])
  for n in range(N+2):
    mapList[h].append([])
    for m in range(M+2):
      mapList[h][n].append(-1)

# 입력에 따라 맵 정보 갱신
for h in range(1, H+1):
  for n in range(1, N+1):
    tempList = list(map(int, sys.stdin.readline().split()))
    for m in range(1,M+1):
      mapList[h][n][m] = tempList[m-1]

result = 0
#BFS탐색 시작

tempQu = deque()

for h in range(1, H+1):
  for n in range(1, N+1):
    for m in range(1,M+1):
      if mapList[h][n][m] == 1:
        tempQu.append((h,n,m,0))

while tempQu:
  curCoord = tempQu.popleft()
  h, n ,m ,d= curCoord[0],  curCoord[1],  curCoord[2], curCoord[3]
  result = max(result, d)
    #좌탐색
  if mapList[h][n][m-1] == 0:
    mapList[h][n][m-1] = 1
    tempQu.append((h,n,m-1,d+1))
  #우탐색
  if mapList[h][n][m+1] == 0:
    mapList[h][n][m+1] = 1
    tempQu.append((h,n,m+1,d+1))
  #앞탐색
  if mapList[h][n+1][m] == 0:
    mapList[h][n+1][m] = 1
    tempQu.append((h,n+1,m,d+1))
  #뒤탐색
  if mapList[h][n-1][m] == 0:
    mapList[h][n-1][m] = 1
    tempQu.append((h,n-1,m,d+1))
  #위탐색
  if mapList[h+1][n][m] == 0:
    mapList[h+1][n][m] = 1
    tempQu.append((h+1,n,m,d+1))
  #아래탐색
  if mapList[h-1][n][m] == 0:
    mapList[h-1][n][m] = 1
    tempQu.append((h-1,n,m,d+1))


#다 안익은 경우 체크
for h in range(1, H+1):
  for n in range(1, N+1):
    for m in range(1,M+1):
      if mapList[h][n][m] == 0:
        result = -1

print(result) 