N = int(input())
coins = list(map(int, input().split()))


targetNum = 1
flag = True # 초기 상태

while(targetNum <= 1000):
    
    for i in range(len(coins)):
        #정수 찾았으면 더 볼 필요없는 상태 : False
        if(flag == False):
            break
        tempNum = targetNum
        for j in range(i, len(coins)):
            tempNum = tempNum - coins[j]
            if(tempNum < 0):
                tempNum += coins[j]
            elif(tempNum == 0):
                flag = False
                break
            
            
            
    if(flag == False):
        flag = True
        targetNum +=1
    else:
        break
    
print(targetNum)
