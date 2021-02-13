strList = []
for i in range(2):
  strList.append(input())

dp = [0] * (len(strList[0])+1) 

curIdx = 0
for i,v in enumerate(strList[0]):
  flag = False
  for j,k in enumerate(strList[1][curIdx:]):
    if v == k:
      flag = True
      dp[i+1] = dp[i] + j
      curIdx = curIdx+ j+1
      break
  
  if flag == False:
    dp[i+1] = dp[i] + 1
    curIdx += 1

print(dp[len(strList[0])] + len(strList[1]) - curIdx)  