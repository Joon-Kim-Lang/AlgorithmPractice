N, K = map(int, input().split())

coinList = []
for _ in range(N):
  coinList.append(int(input()))

result = 0
idx = -1

while True:
  if coinList[idx] <= K:
    K -= coinList[idx]
    result +=1
  else:
    idx -= 1
    continue

  if K == 0:
    break

print(result) 