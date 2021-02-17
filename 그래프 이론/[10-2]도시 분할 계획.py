def find_parent(parent, x):
  if x != parent[x]:
    return find_parent(parent, parent[x])

  return parent[x]

def union_parent(parent, a,b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a > b:
    parent[a] = b
  else:
    parent[b] = a

v, e = map(int, input().split())

parent = [0] * (v+1)

for i in range(1, v+1):
  parent[i] = i

edges = []
result = 0
maxEdge = 0

for _ in range(e):
  a,b,cost = map(int, input().split())
  edges.append((cost,a,b))

edges.sort()

#크루스칼 시작
for edge in edges:
  cost, a, b = edge

  if find_parent(parent, a) == find_parent(parent,b):
    continue
  else:
    union_parent(parent, a,b)
    result += cost
    maxEdge = max(maxEdge, cost)


print(result - maxEdge)