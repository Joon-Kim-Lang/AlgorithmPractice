N = int(input())

num_list = []

while N > 0:
    num = N % 10
    num_list.append(num)
    N = N // 10    

first_sum = 0
second_sum = 0
for i in range(len(num_list)):
    if i < (len(num_list) / 2):
        first_sum += num_list[i]
    else:
        second_sum += num_list[i]
        
if first_sum == second_sum:
    print("LUCKY")
else:
    print("READY")
