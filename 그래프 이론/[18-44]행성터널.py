n = int(input())

planetcord = []
for i in range(n):
  x,y,z = map(int, input().split())
  planetcord.append((x,y,z,i+1))

edges = []
for j in range(3):  
  tempSorted = sorted(planetcord, key = lambda x : x[j])
  for i in range(0,n-1):
    edges.append((abs(tempSorted[i][j] - tempSorted[i+1][j]),tempSorted[i][3],tempSorted[i+1][3]))


def find_parent(parent, x):
  if x != parent[x]:
    return find_parent(parent, parent[x])
  
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent,b)

  if a > b:
    parent[b] = a
  else:
    parent[a] = b

parent = [0]*(n+1)

for i in range(1, n+1):
  parent[i] = i

edges.sort()

result  = 0
for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) == find_parent(parent,b):
    continue
  else:
    union_parent(parent,a,b)
    result+=cost

print(result)