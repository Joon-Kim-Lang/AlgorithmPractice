n = int(input())
hList = list(map(int, input().split()))

hList.sort()

if  len(hList) % 2 == 0:
  print(hList[ len(hList) // 2 -1])
else:
  print(hList[ len(hList) // 2])