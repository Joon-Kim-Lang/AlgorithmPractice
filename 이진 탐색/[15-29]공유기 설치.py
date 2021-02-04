N, C = map(int, input().split())
numList = []
for i in range(N):
  numList.append(int(input()))

numList.sort()

start = 1
end = numList[-1] - numList[0]


result = float('inf')

while start <= end:

  count = 1
  value = numList[0]
  gap = (start + end) // 2

  for i in range(1,N):
    if numList[i] >= value + gap:
      count+=1
      value = numList[i]

  if count >= C:
    start = gap + 1
    result = gap
  
  else:
    end = gap -1

print(result)