n = int(input())
m = int(input())
INF = int(1e9)

mapList = [[INF] * (n+1) for _  in range(n+1)]

for a in range(1, n+1):
  for b in range(1, n+1):
    if a==b:
      mapList[a][b] = 0

for i in range(m):
  f, t, c = map(int, input().split())  
  mapList[f][t] = min(mapList[f][t], c)

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      mapList[a][b] = min(mapList[a][b], mapList[a][k] + mapList[k][b])

for a  in range(1, n+1):
  for b in range(1, n+1):
    if mapList[a][b] == INF:
      print(0, end = ' ')
    else:
      print(mapList[a][b], end = ' ')

  print()