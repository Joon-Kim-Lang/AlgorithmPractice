def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    answer = 0
    flag = True
    while flag:
        for i in range(len(food_times)):
            if(k == 0):
                if food_times[i] == 0:
                    continue
                answer = i +1
                flag = False
                break;
            
            if food_times[i] > 0:
                food_times[i] -= 1
                k-= 1
            
    return answer
