n = int(input())

triangle = []
dpList = []

for i in range(n):
  triangle.append(list(map(int, input().split())))
  dpList.append([0]*(i+1))

#DP 실행
for i,v in enumerate(triangle):
  if i == 0:
    dpList[i][0] = triangle[i][0]
  
  else:
    for j, k in enumerate(v):
      if j == 0:
        dpList[i][j] = k+ dpList[i-1][j]
      elif j == len(v) -1:
        dpList[i][j] = k + dpList[i-1][j-1]
      else:
        dpList[i][j] = k+ max(dpList[i-1][j], dpList[i-1][j-1])

print(max(dpList[n-1]))