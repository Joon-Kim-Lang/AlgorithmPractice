import copy
N, M, K = map(int, input().split())

mapList = []
sharkInfo = {}
dirDict = {}
dirInfo = [[0,0],[-1,0],[1,0],[0,-1],[0,1]]

for i in range(N+2):
  mapList.append([])
  for j in range(N+2):
    mapList[i].append([])

for i in range(N+2):  
  for j in range(N+2):
    if i==0 or i==(N+1) or j ==0 or j== (N+1):
      mapList[i][j].append([-1,-1])

#초기정보 입력받기
for i in range(N):
  tempList = list(map(int, input().split()))
  for j,v in enumerate(tempList):
    if v != 0:
      sharkInfo[v] = [i+1, j+1]
      mapList[i+1][j+1].append([v, K])

startDir = list(map(int, input().split()))

for i in range(M):
  sharkInfo[i+1].append(startDir[i])

#방향우선순위 정보 받기
curNum = 0
for i in range(M*4):
  if i % 4 == 0:
    curNum +=1
    dirDict[curNum] = []
    dirDict[curNum].append([])
  tempList= list(map(int, input().split()))
  dirDict[curNum].append(tempList)


result = 0

#알고리즘 시작
while result <= 1000 and len(sharkInfo) > 1:  

  tempMap = copy.deepcopy(mapList)

  #냄새 하나씩 빼주기
  for i in range(N+2):
    for j in range(N+2):
      if len(mapList[i][j]) > 0:
        if mapList[i][j][0][1] >= 1:
          mapList[i][j][0][1] -=1

  #빈 공간 우선탐색
  for i in sharkInfo:
    isFound = False
    _row,_col, _dir = sharkInfo[i]
    
    for search in dirDict[i][_dir]:
      if len(tempMap[_row + dirInfo[search][0]][_col + dirInfo[search][1]]) == 0:
        mapList[_row + dirInfo[search][0]][_col + dirInfo[search][1]].append([i,K])
        sharkInfo[i][0] = _row + dirInfo[search][0]
        sharkInfo[i][1] = _col + dirInfo[search][1]
        sharkInfo[i][2] = search
        isFound = True
        break
    #빈 공간을 못 찾았다면
    if not isFound:
    #자신의 냄새가 있는 칸 탐색
      for search in dirDict[i][_dir]:
        if tempMap[_row + dirInfo[search][0]][_col + dirInfo[search][1]][0][0] == i:
          mapList[_row + dirInfo[search][0]][_col + dirInfo[search][1]][0][1] = K
          sharkInfo[i][0] = _row + dirInfo[search][0]
          sharkInfo[i][1] = _col + dirInfo[search][1]
          sharkInfo[i][2] = search
          break

  #잡아먹는 경우 생기나 확인
  for i in range(1, N+1):
    for j in range(1,N+1):
      if len(mapList[i][j]) >= 2:
        mapList[i][j]  = sorted(mapList[i][j], key= lambda x: x[0])
        # print(mapList[i][j],i, j)
        for w,v in enumerate(mapList[i][j]):
          if w == 0:
            tempInfo = copy.deepcopy(v)
          else:
            del(sharkInfo[v[0]])
        
        mapList[i][j].clear()
        mapList[i][j].append(tempInfo)

  for i in range(N+2):
    for j in range(N+2):
      if len(mapList[i][j]) > 0:
        if mapList[i][j][0][1] == 0:
          mapList[i][j].clear()  

  result +=1


if result > 1000:
  print(-1)
else:   
  print(result)