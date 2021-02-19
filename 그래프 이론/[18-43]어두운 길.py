n, m = map(int, input().split())

def find_parent(parent, x):
  if x!= parent[x]:
    return find_parent(parent, parent[x])
  
  return parent[x]

def union_parent(parent, a,b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a > b:
    parent[b] = a
  else:
    parent[a] = b

parent = [0] * n

for i in range(n):
  parent[i] = i

edges = []

prevCost = 0
for _ in range(m):
  a, b , cost = map(int, input().split())
  prevCost += cost
  edges.append((cost,a,b))

edges.sort()

postCost=0
for edge in edges:
  cost, a ,b = edge
  
  if find_parent(parent, a) == find_parent(parent,b):
    continue
  else:
    union_parent(parent, a,b)
    postCost += cost

print(prevCost - postCost)