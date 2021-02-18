from collections import deque
import copy

n = int(input())

indegree = [0] * (n+1)
graph =  [[] for _ in range(n+1)]

time = [0] * (n+1)

for i in range(n):
  data = list(map(int,input().split()))
  time[i+1] = data[0]
  for j in data[1:]:
    if j == -1:
      break
    else:
      graph[j].append(i+1)
      indegree[i+1] +=1

qu = deque()
for i in range(1,n+1):
  if indegree[i] == 0 :
    qu.append(i)

print(indegree)

result = copy.deepcopy(time)
while qu:
  curNode = qu.popleft()

  for i in graph[curNode]:
    indegree[i] -=1
    result[i] = max(result[i], result[curNode] + time[i])

    if indegree[i] == 0:
      qu.append(i)

for i in range(1, n+1):
  print(result[i]) 
