from itertools import combinations

N = int(input())

mapList = []

for i in range(N+2):
  mapList.append([])
  for j in range(N+2):
    mapList[i].append('O')

for i in range(1, N+1):
  tempInput = input().split()
  for j in range(1, N+1):
    mapList[i][j] = tempInput[j-1]
#맵 생성 완료

XList = []
TList = []
for i in range(1, N+1):
  for j in range(1, N+1):
    if mapList[i][j] == 'X':
      XList.append([i,j])
    elif mapList[i][j] == 'T':
      TList.append([i,j]) 

XaftComb = list(combinations(XList, 3))

def isSafe(mapList, TList):
  for i in TList:
    #위쪽검사
    upCnt = 1
    while True:
      if mapList[i[0]-upCnt][i[1]] == 'X':
        upCnt+=1
        continue
      elif  mapList[i[0]-upCnt][i[1]] == 'S':
        return False
      else:
        break;
    #아래검사
    dwCnt = 1
    while True:
      if mapList[i[0]+dwCnt][i[1]] == 'X':
        dwCnt+=1
        continue
      elif  mapList[i[0]+dwCnt][i[1]] == 'S':
        return False
      else:
        break;
    #왼쪽검사
    lfCnt = 1
    while True:
      if mapList[i[0]][i[1]-lfCnt] == 'X':
        lfCnt+=1
        continue
      elif  mapList[i[0]][i[1]-lfCnt] == 'S':
        return False
      else:
        break;
    #오른쪽검사
    rtCnt = 1
    while True:
      if mapList[i[0]][i[1]+rtCnt] == 'X':
        rtCnt+=1
        continue
      elif  mapList[i[0]][i[1]+rtCnt] == 'S':
        return False
      else:
        break;
  
  return True

flag = True

for i in XaftComb:
  for j in range(len(i)):
    mapList[i[j][0]][i[j][1]] = 'O'
  
  result = isSafe(mapList,TList)

  if result:
    print('YES')
    flag = False
    break

  for j in  range(len(i)):
    mapList[i[j][0]][i[j][1]] = 'X'

if flag == True:
  print('NO')