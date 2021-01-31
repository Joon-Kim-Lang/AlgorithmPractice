def solution(N, stages):
    curPeople = len(stages)
    tempAns = []
    for i in range(1, N+1):
        #앞에서 미리 끝나버리는 경우
        if curPeople == 0:
            tempAns.append((0, i))
            continue
        failRate = stages.count(i) / curPeople
        tempAns.append((failRate, i))
        curPeople -= stages.count(i)
    
    tempAns = sorted(tempAns, key = lambda x : (-x[0],x[1]))
    answer = []
    for i in tempAns:
        answer.append(i[1])
        
    return answer