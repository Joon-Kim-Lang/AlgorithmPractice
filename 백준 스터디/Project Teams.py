N = int(input())
cpcList = list(map(int, input().split()))

cpcList.sort(reverse=True)

teamList = [0] * N

reverseIdx = -1
for i in range(len(cpcList)):
  if i >= N:
    teamList[reverseIdx] += cpcList[i]
    reverseIdx -= 1
  else:
    teamList[i] += cpcList[i]

print(min(teamList)) 