def solution(p):    

    return uvSplit(p)


def isValid(string):
    openCnt = 0
    closeCnt = 0
    
    for i in string:
        if i == '(':
            openCnt +=1
        elif i == ')':
            closeCnt +=1
            
        if closeCnt > openCnt:
            return False
    
    return True
    

def uvSplit(string):
    if string == '':
        return ''
    
    curOpen = 0
    curClose = 0
    u = ''
    
    for i in string:
        if i == '(':           
            curOpen +=1
            u+='('
        elif i == ')':
            curClose+=1
            u+=')'
        if curOpen == curClose:
            break
            
    v = string[len(u):]
    
    if isValid(u) == True:
        return u + uvSplit(v)
    else:
        tempU = u[1:len(u)-1]
        newU = ''
        for i in range(len(tempU)):
            if tempU[i] == '(':
                newU = newU+ ')'
            else:
                newU = newU+ '('
        return '('+uvSplit(v)+')'+newU