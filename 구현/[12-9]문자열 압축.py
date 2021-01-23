from queue import Queue

def solution(s):
    curShortestLen = 1001
    
    k = 1
    queue = Queue()
    while k <= len(s):
        for i in range(0,len(s),k):
            queue.put(s[i:i+k])
        prevTempStr = ""  
        tempShortestLen = 0
        tempRep = False
        tempRepNum = 0
        while queue.empty() == False :
            tempStr = queue.get().rstrip()

            #앞의 섭스트링과 반복이 아닐경우
            if tempStr != prevTempStr:
                tempShortestLen += len(tempStr)
                prevTempStr = tempStr
                tempRepNum = 1
                tempRep = False
            #앞에 섭스트링과 반복일 경우
            else:
                #반복횟수가 겹치면 안되기 때문에
                tempRepNum+=1
                if tempRepNum == 10:
                    tempShortestLen+=1
                elif tempRepNum == 100:
                    tempShortestLen+=1
                elif tempRepNum == 1000:
                    tempShortestLen+=1
                if tempRep == False:
                    tempShortestLen+=1
                    tempRep = True
        print(tempShortestLen)
        if tempShortestLen < curShortestLen:
            curShortestLen = tempShortestLen
        k+=1
                
                
            
            
    return curShortestLen
