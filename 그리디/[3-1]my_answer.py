N = int(input("얼마를 거슬러 줘야 하나요?:"))

cnt_500 = 0
cnt_100 = 0
cnt_50 = 0
cnt_10 = 0

while(N > 0):
    if N >= 500:
        N -= 500
        cnt_500+=1
        continue
    elif N >= 100:
        N -= 100
        cnt_100+=1
        continue
    elif N >= 50:
        N -= 50
        cnt_50+=1
        continue    
    else:
        N -= 10
        cnt_10+=1
        continue
    
min_changes = cnt_500 + cnt_100 + cnt_50 + cnt_10
print("거스름돈의 최소 개수는",min_changes,"입니다")
