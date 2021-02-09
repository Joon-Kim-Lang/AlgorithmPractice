N,M = map(int, input().split())

monList = []
for i in range(N):
  monList.append(int(input()))

dpList = [10001] * (M+1)
dpList[0] = 0

for i in monList:
  for j in range(i,M+1):
    dpList[j] = min(dpList[j-i]+1, dpList[j])

if dpList[M] == 10001:
  print(-1)
else:
    print(dpList[M])     