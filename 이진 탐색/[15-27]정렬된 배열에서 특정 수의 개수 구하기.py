N, X = map(int, input().split())
numList = list(map(int, input().split()))

def findStart(start, end, target):
  if start > end:
    return 1
  mid = (start + end) // 2
  if numList[mid] < target:
    start = mid + 1
    return findStart(start, end, target)

  elif numList[mid] > target:
    end = mid - 1
    return findStart(start, end, target)

  else:
    if numList[mid-1] == target:
      end = mid - 1
      return findStart(start, end, target)

    else: 
      return mid


def findEnd(start, end, target):
  if start > end:
    return -1
  mid = (start + end) // 2
  if numList[mid] < target:
    start = mid + 1
    return findEnd(start, end, target)

  elif numList[mid] > target:
    end = mid - 1
    return findEnd(start, end, target)

  else:
    if numList[mid+1] == target:
      start = mid + 1
      return findEnd(start, end, target)

    else: 
      return mid

start = findStart(0, len(numList)-1,X)
end = findEnd(0, len(numList)-1,X)

print(end- start +1)