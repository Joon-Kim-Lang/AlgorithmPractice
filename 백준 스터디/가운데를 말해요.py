import heapq

smallQu = []
largeQu = []
heapq.heappush(smallQu, (10001, -10001))
heapq.heappush(largeQu, 10001)

answerList = []

N = int(input())

for _ in range(N):
  curNum = int(input())
  if len(smallQu) == len(largeQu):
    if curNum <= largeQu[0]:
      heapq.heappush(smallQu, (-curNum, curNum))
    else:
      temp = heapq.heappop(largeQu)
      heapq.heappush(smallQu, (-temp, temp))
      heapq.heappush(largeQu, curNum)
  
  else:
    if curNum >= smallQu[0][1]:
      heapq.heappush(largeQu, curNum)
    else:
      temp = heapq.heappop(smallQu)
      heapq.heappush(largeQu, temp[1])
      heapq.heappush(smallQu, (-curNum,curNum))

  answerList.append(smallQu[0][1])

for answer in answerList:
  print(answer)