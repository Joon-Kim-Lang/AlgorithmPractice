N = int(input())

dpList = [0]*10001

dpList[1] = 1
dpList[2] = 3

for i in range(3,N+1):
  dpList[i] = dpList[i-1] + 2*dpList[i-2]

print(dpList[N] % 7967956)
