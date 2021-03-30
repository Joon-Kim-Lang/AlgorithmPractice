N = int(input())
mntList = list(map(int, input().split()))

mntList = sorted(mntList)


answer = 0
curSum = 0

for ele in mntList:
  curSum = curSum + ele
  answer = answer + curSum

print(answer)