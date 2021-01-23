import time

n, m = map(int, input().split())
weights = list(map(int, input().split()))


start_time = time.time()

result = 0

for i in range(n):
    for j in range(i+1, n):
        if weights[i] == weights[j]:
            continue
        else:
            result+=1
            
print(result)

end_time = time.time()   
print("result:",result,"소요시간:",end_time-start_time,"ms")
