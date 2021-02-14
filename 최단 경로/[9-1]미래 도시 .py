v, e = map(int, input().split())

INF = int(1e9)
mapList = [[INF] * (v+1) for _ in range(v+1)]

for a in range(1, v+1):
  for b in range(1, v+1):
    if a == b:
      mapList[a][b] = 0

for i in range(e):
  f, t = map(int, input().split())
  mapList[f][t] = 1
  mapList[t][f] = 1

x, k = map(int, input().split())
#플로이드 워셜 적용
for i in range(1, v+1):
  for a in range(1, v+1):
    for b in range(1, v+1):
      mapList[a][b] = min (mapList[a][b], mapList[a][i] + mapList[i][b])

result = mapList[1][k] + mapList[k][x]

if result > INF:
  print(-1)
else:
  print(result)