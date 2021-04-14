N, M = map(int, input().split())
treeList = list(map(int, input().split()))

start = 1
end = max(treeList)
result = 0

while start <= end:
  mid = (start + end) // 2
  tempRst = 0

  for tree in treeList:
    if (tree - mid) > 0:
      tempRst += (tree - mid)
  
  if tempRst >= M:
    start = mid + 1
    result = max(mid, result)
  else:
    end = mid -1

print(result)