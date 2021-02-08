from bisect import bisect_left, bisect_right

def solution(words, queries):
    
    answer = []
    
    lenList = [[] for _ in range(10001)]
    rvLenList = [[] for _ in range(10001)]
    
    for w in words:
        lenList[len(w)].append(w)
        rvLenList[len(w)].append(w[::-1])
        
    for i in range(len(lenList)):
        lenList[i].sort()
        rvLenList[i].sort()

    for q in queries:
        #접두사에 ?가 붙는 경우
        if q[0] != "?":
            answer.append(count_index(lenList[len(q)], q.replace("?","a"), q.replace("?","z")))
        else:
            answer.append(count_index(rvLenList[len(q)], q[::-1].replace("?","a"), q[::-1].replace("?","z")))       
    return answer

def count_index(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    return right_index - left_index