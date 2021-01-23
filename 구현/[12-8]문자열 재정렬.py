string = input()

alpahbetList = []
numList = ['0','1','2','3','4','5','6','7','8','9']
numSum = 0
for i in string:
    if i not in numList:
        alpahbetList.append(i)
    else:
        numSum += int(i)
        
alpahbetList.sort()


final_str = ''

for i in alpahbetList:
    final_str  = final_str+i
    
final_str = final_str + str(numSum)

print(final_str)
