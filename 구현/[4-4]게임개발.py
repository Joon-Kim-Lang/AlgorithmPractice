#N이 세로, M이 가로
N, M = map(int, input().split())
conditions = list(map(int, input().split()))

print(N,M,conditions)

map_info = []
for i in range(N):
    map_info.append(list(map(int, input().split())))
    
print(map_info)

#세로
curX = conditions[0]
#가로
curY = conditions[1]
curDir = conditions[2]

result = 1

flag = True
flag_cnt = 0

while(flag):
    #북쪽일때
    if curDir == 0:
        map_info[curX][curY] = -1
        curDir = 3
        flag_cnt+=1
        if map_info[curX][curY -1] == 0:
            curY -=1
            result+=1
            flag_cnt=0
            continue
        if flag_cnt == 5:
            if map_info[curX+1][curY] != 1:
                curX += 1
                flag_cnt = 0
            else:
                flag = False
    #서쪽일때    
    if curDir == 3:
        map_info[curX][curY] = -1
        curDir = 2
        flag_cnt+=1
        if map_info[curX+1][curY] == 0:
            curX+=1
            result+=1
            flag_cnt=0
            continue
        if flag_cnt == 5:
            if map_info[curX][curY+1] != 1:
                curY += 1
                flag_cnt = 0
            else:
                flag = False
    #남쪽일때    
    if curDir == 2:
        map_info[curX][curY] = -1
        curDir = 1
        flag_cnt+=1
        if map_info[curX][curY+1] == 0:
            curY+=1
            result+=1
            flag_cnt=0
            continue
        if flag_cnt == 5:
            if map_info[curX-1][curY] != 1:
                curX -= 1
                flag_cnt = 0
            else:
                flag = False
    #동쪽일때    
    if curDir == 1:
        map_info[curX][curY] = -1
        curDir = 0
        flag_cnt+=1
        if map_info[curX-1][curY] == 0:
            curX-=1
            result+=1
            flag_cnt=0
            continue
        if flag_cnt == 5:
            if map_info[curX][curY-1] != 1:
                curY -= 1
                flag_cnt = 0
            else:
                flag = False
                
print(result)
