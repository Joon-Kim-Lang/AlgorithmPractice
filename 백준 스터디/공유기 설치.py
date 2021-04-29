N, C = map(int, input().split())

numList = []

for _ in range(N):
  numList.append(int(input()))

numList.sort()

start = 1
end = numList[-1] - numList[0]
result = 0

while start <= end:

  gap = (start + end) // 2
  count = 1
  value = numList[0]
  
  for i in range(1, len(numList)):
    if numList[i] >= value + gap:
      count +=1
      value = numList[i]

  if count >= C:
    result = gap
    start = gap +1
  else:
    end = gap - 1

print(result)