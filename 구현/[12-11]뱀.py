import collections 

N = int(input())
appleCnt = int(input())

appleCorList = []
for i in range(appleCnt):
  tempList = list(map(int, input().split()))
  appleCorList.append(tempList)

rotationCnt = int(input())
rotationInfo = []
for i in range(rotationCnt):
  tempList = list(input().split())
  tempList[0] = int(tempList[0])
  rotationInfo.append(tempList)

#인풋 입력 종료

mapList= []
for i in range(N+2):
  mapList.append([])
  for j in range(N+2):
    if i == 0 or j == 0 or i == N+1 or j == N+1:
      mapList[i].append(0)
    else:
      mapList[i].append(1)

for i in range(appleCnt):
  mapList[appleCorList[i][0]][appleCorList[i][1]] =2

mapList[1][1] =3
#맵 생성종료

curSnake = collections.deque() 
curSnake.append([1,1])
dir_map = {"east" : [0,1], "west":[0,-1],"south":[1,0],"north":[-1,0]}
direction =dir_map["east"]
dir_str = "east"
timespent = 0

while(True):

  for i in range(len(mapList)):
    print(mapList[i])
  print(timespent)

  #다음 움직임이 벽일경우
  if mapList[curSnake[0][0]+ direction[0]][curSnake[0][1]+direction[1]] == 0:
    timespent+=1
    break
  #다음 움직임 부분이 1일 경우
  elif mapList[curSnake[0][0]+ direction[0]][curSnake[0][1]+direction[1]] == 1:
    mapList[curSnake[0][0]+ direction[0]][curSnake[0][1]+direction[1]] = 3
    curSnake.appendleft([curSnake[0][0]+ direction[0],curSnake[0][1]+direction[1]])
    removedCord = curSnake.pop()
    mapList[removedCord[0]][removedCord[1]] = 1
  #사과를 먹을경우
  elif mapList[curSnake[0][0]+ direction[0]][curSnake[0][1]+direction[1]] == 2:
    mapList[curSnake[0][0]+ direction[0]][curSnake[0][1]+direction[1]] = 3
    curSnake.appendleft([curSnake[0][0]+ direction[0],curSnake[0][1]+direction[1]])
  #다음 움직임이 자신의 몸통일경
  elif mapList[curSnake[0][0]+ direction[0]][curSnake[0][1]+direction[1]] == 3:
    timespent+=1
    break

  timespent +=1

  for i in range(len(rotationInfo)):
    if rotationInfo[i][0] == timespent:
      if dir_str == "east":
        if rotationInfo[i][1] == "D":
          dir_str = "south"
          direction = dir_map[dir_str]
        else:
          dir_str = "north"
          direction = dir_map[dir_str]

      elif dir_str == "west":
        if rotationInfo[i][1] == "D":
          dir_str = "north"
          direction = dir_map[dir_str]
        else:
          dir_str = "south"
          direction = dir_map[dir_str]

      elif dir_str == "north":
        if rotationInfo[i][1] == "D":
          dir_str = "east"
          direction = dir_map[dir_str]
        else:
          dir_str = "west"
          direction = dir_map[dir_str]

      elif dir_str == "south":
        if rotationInfo[i][1] == "D":
          dir_str = "west"
          direction = dir_map[dir_str]
        else:
          dir_str = "east"
          direction = dir_map[dir_str]




print(timespent)
