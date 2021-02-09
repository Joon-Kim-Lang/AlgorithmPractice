T = int(input())

#맵 생성 완료
resultList = []
for i in range(T):
  mapList = []
  dpList = []
  n, m = map(int, input().split())
  for j in range(n+2):
    mapList.append([0]*(m+2))
    dpList.append([0]*(m+2))

  goldList = list(map(int, input().split()))
  
  for i,v in enumerate(goldList):
    row = (i // 4) + 1
    col = (i % 4) +1
    mapList[row][col] = v



#DP 알고리즘 시작
  for i in range(1, m+1):
    for j in range(1, n+1):
      dpList[j][i] = max(dpList[j-1][i-1],dpList[j][i-1],dpList[j+1][i-1]) + mapList[j][i]
  result = 0
  for i in range(1, n+1):
    result = max(result,dpList[i][m])
  resultList.append(result)

for i in resultList:
  print(i)