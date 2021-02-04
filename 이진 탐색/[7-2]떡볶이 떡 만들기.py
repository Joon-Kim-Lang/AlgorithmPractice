N, M  = map(int, input().split())
cakeList = list(map(int, input().split()))

cakeList = sorted(cakeList, reverse = True)

curEnd = cakeList[0]
curStart = 0
curAble = 0
curPivot = 0
result = 0

while curStart <= curEnd:
  curAble = 0
  curPivot = (curEnd + curStart) // 2

  for i in cakeList:
    if i > curPivot:
      curAble += i - curPivot
    else:
      continue  
    
  if curAble >= M:
    result = curPivot
    curStart = curPivot +1
  else:
    curEnd = curPivot -1

print(result)

