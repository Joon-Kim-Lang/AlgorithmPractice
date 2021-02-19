gates = int(input())
planes = int(input())

graph = [[] for _ in range(gates+1)]
indegree = [0] *(gates+1)

for i in range(1, gates+1):
  indegree[i] = i

for i in range(1,gates+1):
  for j in range(gates -i):
    graph[i].append(gates-j)

result = 0
flag = False

for _ in range(planes):
  avbGate = int(input())
  if flag:
    continue
  if indegree[avbGate] == 0:
    flag = True
    continue
  else:
    result+=1
    indegree[avbGate] -=1

    for i in graph[avbGate]:
      indegree[i] -= 1

print(result)