N = int(input())
meetingList = []
for _ in range(N):
  start, end = map(int, input().split())
  meetingList.append((start,end))

meetingList = sorted(meetingList, key = lambda x: (-x[1],-x[0]))

curEnd = -1
curStart = int(2**31)
result = 0

for i in meetingList:
  start, end = i

  if end <= curStart:
    curEnd = end
    curStart = start
    result += 1
  else:
    if start > curStart:
      curEnd = end
      curStart = start

print(result)