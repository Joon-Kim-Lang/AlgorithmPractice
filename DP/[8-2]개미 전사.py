N  = int(input())

dpList =  [0] * 101

foodList = list(map(int, input().split()))
dpList[1] = foodList[0]

for i in range(2, N+1):
  dpList[i] = max(dpList[i-2]+foodList[i-1], dpList[i-1])

print(dpList[N])