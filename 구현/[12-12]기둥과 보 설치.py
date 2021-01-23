def solution(n, build_frame):
    
    answer = []
    for x,y,kind,action in build_frame:
        tempInput = [x,y,kind]
        #설치일경우
        if action == 1: 
            answer.append(tempInput)
            if isPossible(answer) == False:
                answer.remove(tempInput)
                
        #삭제일경우        
        else:
            answer.remove(tempInput)
            if isPossible(answer) != True:
                answer.append(tempInput)           
    
    answer.sort(key=lambda x:(x[0],x[1],x[2]))
    return answer

def isPossible(curState):
    
    for x, y, kind in curState:
        #기둥일 경우
        if kind == 0:
            if (y == 0) or ([x,y-1,0] in curState)  or ([x-1,y,1] in curState) or ([x,y,1] in curState):
                continue
            return False
        
        elif kind == 1:
            if ([x,y-1,0] in curState) or ([x+1,y-1,0] in curState) or (([x-1,y,1] in curState) and ([x+1,y,1] in curState)):
                continue
            return False
    return True
            
    
