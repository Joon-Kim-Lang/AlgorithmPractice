N = int(input())
numList = list(map(int, input().split()))

def findFxPoint(start, end):

  if start > end:
    return -1

  mid = (end+start) // 2

  if numList[mid] < 0:
    start = mid+1
    return  findFxPoint(start,end)
  
  elif numList[mid] > len(numList) -1:
    end = mid -1
    return findFxPoint(start, end)

  elif numList[mid] == mid:
    return mid

  else:
    tempRst = findFxPoint(mid+1, end)
    if tempRst != -1:
      return tempRst
    else:
      return findFxPoint(start, mid-1)

print(findFxPoint(0, len(numList) -1))
