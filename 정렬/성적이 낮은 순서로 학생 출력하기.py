N = int(input())

stuList = []
for i in range(N):
  stuList.append(input().split())
  stuList[i][1] = int(stuList[i][1])

stuList = sorted(stuList, key= lambda student : student[1])

for i in stuList:
  print(i[0], end = ' ')