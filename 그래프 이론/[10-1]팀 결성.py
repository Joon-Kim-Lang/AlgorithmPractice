def find_parent(parent,x):
  if x != parent[x]:
    return find_parent(parent, parent[x])

  return parent[x]

def union_parent(parent, a, b):
  a= find_parent(parent, a)
  b= find_parent(parent, b)

  if a > b:
    parent[a] = b
  else:
    parent[b] = a

n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(1, n+1):
  parent[i] = i 

result= []

for _ in range(m):
  f, a, b = map(int, input().split())

  if f == 0:
    union_parent(parent,a,b)
  else:
    if find_parent(parent, a) == find_parent(parent, b):
      result.append("YES")
    else:
      result.append("NO")

for i in result:
  print(i)