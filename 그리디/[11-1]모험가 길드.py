import time

start_time = time.time()

n = int(input())
people = list(map(int, input().split()))


cur_courage = 1
leftover = 0
result = 0

max_courage = max(people)

while(cur_courage <= max_courage):
    result += (people.count(cur_courage) + leftover) // cur_courage
    leftover = (people.count(cur_courage) + leftover) % cur_courage
    cur_courage+=1
    
end_time = time.time()   
print("result:",result,"소요시간:",end_time-start_time,"ms")
