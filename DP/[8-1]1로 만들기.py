n = int(input())

dpList = [0]*30001

for i in range(2, n+1):
  dpList[i] = dpList[i-1] +1

  if i % 2 == 0:
    dpList[i] = min(dpList[i], dpList[i//2]+1)

  if i % 3 == 0:
    dpList[i] = min(dpList[i], dpList[i//3]+1)

  if i % 5 == 0:
    dpList[i] = min(dpList[i], dpList[i//5]+1)


print(dpList[n])
