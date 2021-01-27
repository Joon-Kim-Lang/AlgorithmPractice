from itertools import permutations

N = int(input())

num_list = list(map(int, input().split()))

op_list = list(map(int,input().split()))

#연산자 콤비네이션 만들기
opForComb = []
for i in range(len(op_list)):
  for j in range(op_list[i]):
    if i == 0:
      opForComb.append('add')
    elif i == 1:
      opForComb.append('sub')
    elif i ==2:
      opForComb.append('mul')
    else:
      opForComb.append('div')

combRst = list(set(permutations(opForComb,len(opForComb))))

maxRst = -float("inf")
minRst = float("inf")

for i in range(len(combRst)):
  curNum = num_list[0]
  curCnt = 1
  for j in combRst[i]:
    if j == "add":
      curNum = curNum + num_list[curCnt]
    elif j == "sub":
      curNum = curNum - num_list[curCnt]
    elif j == "mul":
      curNum = curNum * num_list[curCnt]
    else:
      if (curNum < 0 and num_list[curCnt] > 0) or (curNum > 0 and num_list[curCnt] < 0):
        curNum = -1 * (abs(curNum) // abs(num_list[curCnt]))
      else:
        curNum = curNum // num_list[curCnt]
    curCnt+=1
  
  maxRst = max(maxRst, curNum)
  minRst = min(minRst, curNum)

print(maxRst)
print(minRst)