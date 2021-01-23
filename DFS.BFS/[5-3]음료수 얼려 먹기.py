N, M = map(int, input().split())

#아이스박스 생성
iceBox = []
for i in range(N+2):
  iceBox.append([])
  for j in range(M+2):
    iceBox[i].append(1)

for i in range(1, N+1):
  tempStr = input()
  for j in range(1, M+1):
    iceBox[i][j] = int(tempStr[j-1])

stack = []

def putNeighbors(iceBox, cor):
  #위방향
  if iceBox[cor[0]-1][cor[1]] == 0:
    stack.append([cor[0]-1,cor[1]])
  #아래방향
  if iceBox[cor[0]+1][cor[1]] == 0:
    stack.append([cor[0]+1,cor[1]])
  #오른쪽
  if iceBox[cor[0]][cor[1]+1] == 0:
    stack.append([cor[0],cor[1]+1])
  #왼쪽
  if iceBox[cor[0]][cor[1]-1] == 0:
    stack.append([cor[0],cor[1]-1])

iceCnt = 0

for i in range(1,N+1):
  for j in range(1, M+1):
    if iceBox[i][j] == 0:
      iceBox[i][j] = 1
      stack.append([i,j])
      while len(stack) > 0:
        curCor = stack.pop()
        iceBox[curCor[0]][curCor[1]] = 1
        putNeighbors(iceBox,curCor)
      iceCnt+=1

print(iceCnt)
        

