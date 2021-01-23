number = input()

zeroCnt = 0
oneCnt = 0
curNum = -1

for i in number:
    if int(i) != curNum:
        curNum =int(i)
        if curNum == 0:
            zeroCnt+=1
        else:
            oneCnt+=1
            
result = min(zeroCnt,oneCnt)
print(result)
