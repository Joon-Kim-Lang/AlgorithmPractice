from collections import deque

N = int(input())
M = int(input())

connectedList = [[] for _ in range(N+1)]

for _ in range(M):
  n1, n2 = map(int, input().split())
  connectedList[n1].append(n2)
  connectedList[n2].append(n1)

isVisited = [False] * (N+1)

#DFS 수행
dfsRst = []
dfsQu = deque()
dfsQu.append(1)
isVisited[1] = True

def DFS(qu):
  if len(qu) == 0:
    return

  curNode = qu.popleft()
  dfsRst.append(curNode)
  
  tempList = connectedList[curNode]
  tempList = sorted(tempList)
  for child in tempList:
    if isVisited[child] == False:
      isVisited[child] = True
      qu.append(child)
      DFS(qu)

DFS(dfsQu)

print(len(dfsRst)-1)