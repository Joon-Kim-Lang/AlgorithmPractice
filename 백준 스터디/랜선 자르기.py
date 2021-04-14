N, K  = map(int, input().split())

lineList = []

for _ in range(N):
  lineList.append(int(input()))

start = 1
end = max(lineList)
result = 0

while start <= end:
  mid = (end + start) // 2

  tmpresult = 0

  for line in lineList:
    tmpresult += (line // mid)

  if tmpresult >= K:
    start = mid + 1
    result = max(mid, result)
  else:
    end = mid - 1

print(result)