def solution(s):
    
    answer = 1001
    
    for i in range(1, len(s)): 
        curIdx = 0
        tempRst = 0
        curLen = 1
        while curIdx < len(s):
            #새로운게 잡히는 경우
            if curLen == 1:
                if s[curIdx:curIdx+i] == s[curIdx+i:curIdx+(i*2)]:
                    curLen += 1
                    tempRst+= i
                    curIdx +=i
                else:
                    tempRst += len(s[curIdx:curIdx+i].rstrip())
                    curIdx += i
            #연속된 값이 잡혔던 경우
            else:
                if s[curIdx:curIdx+i] == s[curIdx+i:curIdx+(i*2)]:
                    curLen +=1
                    curIdx +=i
                else:                    
                    tempRst += len(str(curLen))
                    curLen = 1
                    curIdx+=i                
        
        answer = min(answer, tempRst)
        
    if len(s) == 1:
        answer = 1
        
    return answer