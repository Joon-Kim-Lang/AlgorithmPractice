import copy


def solution(key, lock):
    #3배짜리 자물쇠 생성
    bigLock = []
    for i in range(len(lock)*3):
        bigLock.append([])
        for j in range(len(lock)*3):
            bigLock[i].append(0)

    #3배 자물쇠 중간에 원래 자물쇠 끼워넣기
    for i in range(len(lock), len(lock)*2):
        for j in range(len(lock), len(lock)*2):
            bigLock[i][j] = lock[i - len(lock)][j - len(lock)]            
    
    for i in range(0, len(bigLock)-len(key)):
        for j in range(0, len(bigLock)-len(key)):
            for rotation in range(4):
                key = rotateKey(key)
                
                keyRowIndex = -1                
                for k in range(i, i+len(key)):
                    keyRowIndex+=1
                    keyColIndex = 0
                    for s in range(j, j+ len(key)):
                        bigLock[k][s] += key[keyRowIndex][keyColIndex]
                        keyColIndex+=1
                result = check(bigLock, len(lock))
                if result == True:
                    return True
                else:
                    keyRowIndex = -1                
                    for k in range(i, i+len(key)):
                        keyRowIndex+=1
                        keyColIndex = 0
                        for s in range(j, j+ len(key)):
                            bigLock[k][s] -= key[keyRowIndex][keyColIndex]
                            keyColIndex+=1
        
    return False

def check(bigLock, lockLen):
    for i in range(lockLen, lockLen*2):
        for j in range(lockLen, lockLen*2):
            if bigLock[i][j] != 1:
                return False
    return True
    
    

def rotateKey(key):
    key = copy.deepcopy(key)
    rotatedKey = []
    for i in range(len(key)):
        tempList = []
        for j in range(len(key)):
            tempList.append(key[j][i])
        tempList.reverse()
        rotatedKey.append(tempList)
    
    return rotatedKey
