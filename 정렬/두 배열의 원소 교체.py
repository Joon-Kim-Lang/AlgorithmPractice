N, K = map(int, input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

for i in range(K):
  a = min(A)
  b = max(B)

  if a < b :
    A.remove(a)
    A.append(b)
    B.remove(b)
    B.append(a)
  else:
    break

print(sum(A))
