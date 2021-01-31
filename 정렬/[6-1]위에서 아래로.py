N = int(input())

numList = []
for i in range(N):
  numList.append(int(input()))

numList.sort(reverse = True)

for i in numList:
  print(i, end=' ')
