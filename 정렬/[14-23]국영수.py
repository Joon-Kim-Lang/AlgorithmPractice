N = int(input())

stuList = []
for i in range(N):
  tempInput = list(input().split())
  tempInput[1] = int(tempInput[1])
  tempInput[2] = int(tempInput[2])
  tempInput[3] = int(tempInput[3])
  stuList.append(tempInput)

#국어 성적대로
stuList = sorted(stuList, key=lambda x: (-x[1],x[2],-x[3],x[0]))

for i in range(N):
  print(stuList[i][0])