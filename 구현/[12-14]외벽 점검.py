from itertools import permutations

def solution(n, weak, dist):
    
    length = len(weak)
   #길이를 두 배 늘린 배열을 생성
    for i in range(length):
        weak.append(weak[i] + n)
        
    answer = len(dist) + 1
    
    for start in range(length):
        
        for friends in list(permutations(dist, len(dist))):
            count = 1
            
            position = weak[start] + friends[0]
            
            for index in range(start, start + length):
                if position < weak[index]:
                    count+=1
                    if count > len(friends):
                        break
                    position = weak[index] + friends[count-1]
                    
            answer = min(answer,count)
            
    if answer > len(dist):
        answer = -1
        
    return answer
    
    
