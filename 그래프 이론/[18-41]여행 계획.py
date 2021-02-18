n, m = map(int, input().split())

def find_parent(parent, x):
  if x != parent[x]:
    return find_parent(parent, parent[x])
  
  return parent[x]

def union_parent(parent, a,b ):
  a = find_parent(parent,a)
  b = find_parent(parent,b)

  if a > b:
    parent[a] = b
  else:
    parent[b] = a

parent = [0] * (n+1)

for i in range(1, n+1):
  parent[i] = i

for i in range(n):
  temp = list(map(int, input().split()))
  for j in temp:
    if j == 1:
      union_parent(parent, i+1, j+1)

planPath = list(map(int, input().split()))

result = "YES"

for i in range(1, len(planPath)-1):
  if parent[i] != parent[i+1]:
    result = "NO"
    break

print(result)