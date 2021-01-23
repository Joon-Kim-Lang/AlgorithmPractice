numbers = input()
each_number = []

for i in range(len(numbers)):
    each_number.append(int(numbers[i]))

result = 0

for i  in range(len(each_number)):
    #초기값 설정
    if i == 0:
        result += each_number[i]
        continue
    #앞쪽까지의 결과가 0이나 1일 경우 (+)
    if (result == 0) or (result == 1):
        result += each_number[i]
    #현재 숫자가 0이나 1일 경우 (+)    
    elif (each_number[i] == 0) or  (each_number[i] == 1):
        result += each_number[i]
    #현재 숫자가 그 외 숫자일경우(x)    
    else:
        result *= each_number[i]
        
print(result)
