T = int(input())

resultList = []


#테스트 케이스 
for _ in range(T):
  N = int(input())

  parList = [[] for _ in range(N+1)]
  lenList = [[] for _ in range(N)]

  tempList = list(map(int, input().split()))
  
  for i in range(N):
    for j in range(i):
      parList[tempList[i]].append(tempList[j])

  M = int(input())
  #순위 입력값대로 스위칭
  for _ in range(M):
    a, b = map(int, input().split())
    
    if a in parList[b]:
      parList[a].append(b)
      parList[b].remove(a)
    else:
      parList[b].append(a)
      parList[a].remove(b)

  #길이에 따라 정렬
  for i in range(1, N+1):
    lenList[len(parList[i])].append(i)

  tempRstList = []
  impossible = False

  #불능 판정 로직 
  for i,v in enumerate(lenList):
    if len(v) == 1:
      tempRstList.append(v[0])
    elif len(v) > 1:
      tempRstList = "IMPOSSIBLE"
      break

  resultList.append(tempRstList)

for v in resultList:
  if v == "IMPOSSIBLE":
    print(v)
    continue
  
  for i, k in enumerate(v):
    if i == len(v) -1:
      print(k, end='\n')
    else:
      print(k, end=' ')