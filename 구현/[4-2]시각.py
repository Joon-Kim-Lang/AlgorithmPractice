N = int(input())

curH = 0
curM = 0
curS = 0

result = 0

while(curH <= N):
    
    if ('3' in str(curH)) or ('3' in str(curM)) or ('3' in str(curS)):
        result +=1
    
    curS+=1

    if curS == 60:
        curM +=1
        curS = 0
        
    if curM == 60:
        curH +=1
        curM =0
        
print(result) 
