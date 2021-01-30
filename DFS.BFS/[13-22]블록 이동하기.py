import copy
from collections import deque

def solution(board):
    newBoard = []
    for i in range(len(board)+2):
        newBoard.append([])
        for j in range(len(board)+2):
            newBoard[i].append(1)

    for i in range(1,len(board)+1):
        for j in range(1,len(board)+1):
            newBoard[i][j] = board[i-1][j-1]
    
    answer = 10000
    queue = deque()
    newBoard[1][1] = 1
    newBoard[1][2] = 1
    queue.append([newBoard, [1,1,1,2],0,'H'])
    while queue:
        answer = min(answer, findPath(queue))
    return answer

def findPath(queue):
    #curBoard,curPos,curDepth,curDir 담겨야함
    curInfo = queue.popleft()
    curBoard = curInfo[0]
    curPos = curInfo[1] #두 칸(H시 왼오 V시 위아)
    curDepth = curInfo[2]
    curDir = curInfo[3]

    
    #답에 도착인경우
    if curBoard[len(curBoard)-2][len(curBoard)-2] == 1:
        return curDepth
    
    if curDir == 'H':

        if curBoard[curPos[0]-1][curPos[1]] == 0 and curBoard[curPos[2]-1][curPos[3]] == 0:
            newCurBoard = copy.deepcopy(curBoard)
            newCurBoard[curPos[0]-1][curPos[1]] = 1
            newCurBoard[curPos[2]-1][curPos[3]] = 1
            queue.append([newCurBoard, [curPos[0]-1,curPos[1],curPos[2]-1,curPos[3]],curDepth+1,'H'])
            queue.append([newCurBoard, [curPos[0]-1,curPos[1]+1,curPos[2],curPos[3]],curDepth+1,'V'])
            queue.append([newCurBoard, [curPos[0]-1,curPos[1],curPos[0],curPos[1]],curDepth+1,'V'])
        
        #아래쪽이 공백
        if curBoard[curPos[0]+1][curPos[1]] == 0 and curBoard[curPos[2]+1][curPos[3]] == 0:
            newCurBoard = copy.deepcopy(curBoard)
            newCurBoard[curPos[0]+1][curPos[1]] = 1
            newCurBoard[curPos[2]+1][curPos[3]] = 1
            queue.append([newCurBoard, [curPos[0]+1,curPos[1],curPos[2]+1,curPos[3]],curDepth+1,'H'])
            queue.append([newCurBoard, [curPos[0],curPos[1],curPos[2]+1,curPos[3]-1],curDepth+1,'V'])
            queue.append([newCurBoard, [curPos[2],curPos[3],curPos[0]+1,curPos[1]+1],curDepth+1,'V'])
            
        #왼쪽이 공백
        if curBoard[curPos[0]][curPos[1]-1] == 0:
            newCurBoard = copy.deepcopy(curBoard)
            newCurBoard[curPos[0]][curPos[1]-1] = 1
            queue.append([newCurBoard, [curPos[0],curPos[1]-1,curPos[2],curPos[3]-1],curDepth+1,'H'])
        #오른쪽이 공백
        if curBoard[curPos[2]][curPos[3]+1] == 0:
            newCurBoard = copy.deepcopy(curBoard)
            newCurBoard[curPos[2]][curPos[3]+1] = 1
            queue.append([newCurBoard, [curPos[0],curPos[1]+1,curPos[2],curPos[3]+1],curDepth+1,'H'])
            
            
    else:
        #왼쪽이 공백
        if curBoard[curPos[0]][curPos[1]-1] == 0 and curBoard[curPos[2]][curPos[3]-1] == 0:
            newCurBoard = copy.deepcopy(curBoard)
            newCurBoard[curPos[0]][curPos[1]-1] = 1
            newCurBoard[curPos[2]][curPos[3]-1] = 1
            queue.append([newCurBoard, [curPos[0],curPos[1]-1,curPos[2],curPos[3]-1],curDepth+1,'V'])
            queue.append([newCurBoard, [curPos[0],curPos[1]-1,curPos[0],curPos[1]],curDepth+1,'H'])
            queue.append([newCurBoard, [curPos[2],curPos[3]-1,curPos[2],curPos[3]],curDepth+1,'H'])
        #오른쪽이 공백
        if curBoard[curPos[0]][curPos[1]+1] == 0 and curBoard[curPos[2]][curPos[3]+1] == 0:
            newCurBoard = copy.deepcopy(curBoard)
            newCurBoard[curPos[0]][curPos[1]+1] = 1
            newCurBoard[curPos[2]][curPos[3]+1] = 1
            queue.append([newCurBoard, [curPos[0],curPos[1]+1,curPos[2],curPos[3]+1],curDepth+1,'V'])
            queue.append([newCurBoard, [curPos[0],curPos[1],curPos[0],curPos[1]+1],curDepth+1,'H'])
            queue.append([newCurBoard, [curPos[2],curPos[3],curPos[2],curPos[3]+1],curDepth+1,'H'])
            
        #위쪽이 공백
        if curBoard[curPos[0]-1][curPos[1]] == 0:
            newCurBoard = copy.deepcopy(curBoard)
            newCurBoard[curPos[0]-1][curPos[1]] = 1
            queue.append([newCurBoard, [curPos[0]-1,curPos[1],curPos[2]-1,curPos[3]],curDepth+1,'V'])
        #아래쪽이 공백
        if curBoard[curPos[2]+1][curPos[3]] == 0:
            newCurBoard = copy.deepcopy(curBoard)
            newCurBoard[curPos[2]+1][curPos[3]] = 1
            queue.append([newCurBoard, [curPos[0]+1,curPos[1],curPos[2]+1,curPos[3]],curDepth+1,'V'])
            
    return 10000