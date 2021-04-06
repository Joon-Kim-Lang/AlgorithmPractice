from collections import deque

N , M, V = map(int, input().split())

connectedList = [[] for _ in range(N+1)]

for _ in range(M):
  n1, n2 = map(int, input().split())
  connectedList[n1].append(n2)
  connectedList[n2].append(n1)

isVisitedD = [False] * (N+1)
isVisitedB = [False] * (N+1)

#DFS 수행
dfsRst = []
dfsQu = deque()
dfsQu.append(V)
isVisitedD[V] = True

def DFS(qu):
  if len(qu) == 0:
    return

  curNode = qu.popleft()
  dfsRst.append(curNode)
  
  tempList = connectedList[curNode]
  tempList = sorted(tempList)
  for child in tempList:
    if isVisitedD[child] == False:
      isVisitedD[child] = True
      qu.append(child)
      DFS(qu)

DFS(dfsQu)

#BFS 수행
bfsRst = []
bfsQu = deque()
bfsQu.append(V)
isVisitedB[V] = True

while bfsQu:
  curNode = bfsQu.popleft()
  bfsRst.append(curNode)

  tempList = connectedList[curNode]
  tempList = sorted(tempList)

  for child in tempList:
      if isVisitedB[child] == False:
        isVisitedB[child] = True
        bfsQu.append(child)

for ele in dfsRst:
  print(ele, end=" ")
print()
for ele in bfsRst:
  print(ele, end=" ")