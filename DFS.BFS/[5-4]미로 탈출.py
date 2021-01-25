N, M = map(int, input().split())

#맵생성
mapList = []
for i in range(N+2):
  mapList.append([])
  for j in range(M+2):
    mapList[i].append(0)

for i in range(1, N+1):
  tempInput = input()
  for j in range(1, M+1):
    mapList[i][j] = int(tempInput[j-1])


def roadCheck(mapList, queue):
  curCor = queue.pop(0)

  x = curCor[0]
  y = curCor[1]
  length = curCor[2]

  #여기서 도착점이면 그냥 끝내고 반환
  if x == N and y == M:
    return [False, length]

  else:
    mapList[x][y] = 0
    #북쪽
    if mapList[x-1][y] == 1:
      queue.append([x-1,y,length+1])
    #남쪽
    if mapList[x+1][y] == 1:
      queue.append([x+1,y,length+1])
    #서쪽
    if mapList[x][y-1] == 1:
      queue.append([x,y-1,length+1])
    #동쪽
    if mapList[x][y+1] == 1:
      queue.append([x,y+1,length+1])
  
  return [True, length]  

queue = []
queue.append([1,1,1])
flag = True

while(flag):
  result = roadCheck(mapList,queue)

  if result[0] == False:
    print(result[1])
    break
  






