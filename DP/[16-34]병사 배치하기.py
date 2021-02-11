N  = int(input())

strList = list(map(int,input().split()))
strList.reverse()

dp = [1] *(N+1)


for i in range(1,N+1):

  for j in range(i-1,0,-1):
    if strList[i-1] > strList[j-1]:
      dp[i] = max(dp[i], dp[j]+1)


print(N - max(dp))