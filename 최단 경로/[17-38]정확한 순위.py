n, m = map(int, input().split())
INF = int(1e9)

mapList = [[INF] *(n+1) for _ in range(n+1)]

for a in range(n+1):
  for b in range(n+1):
    if a == b:
      mapList[a][b] = 0 

for _ in range(m):
  l, h = map(int, input().split())
  mapList[l][h] = 1

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      mapList[a][b] = min(mapList[a][b], mapList[a][k] + mapList[k][b])

result = 0

for a in range(1, n+1):
  flag = True
  for b in range(1, n+1):
    if a==b: 
      continue

    if mapList[a][b] == INF and mapList[b][a] == INF:
      flag = False
      break
  
  if flag == True:
    result+=1

print(result)