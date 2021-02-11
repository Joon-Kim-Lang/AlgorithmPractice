N = int(input())
infoList = []
infoList.append([0,0])
for i in range(N):
  infoList.append(list(map(int,input().split())))

dpList = [0] * (N+2)

#dp시작

max_val = 0
for i in range(N, 0, -1):
  if i + infoList[i][0] > N+1:
    dpList[i] = max_val
    continue

  dpList[i] = max(infoList[i][1] + dpList[i + infoList[i][0]], max_val)
  max_val = dpList[i]

print(dpList[1])