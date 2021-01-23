cord = input()

alp_dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

print(cord)

curX = alp_dict[cord[0]]
curY = int(cord[1])

result = 0


#왼수평2 위수직1:
if (1<= (curX -2) <=8) and (1<= (curY +1) <=8):
    result+=1
if (1<= (curX -2) <=8) and (1<= (curY -1) <=8):
    result+=1
if (1<= (curX +2) <=8) and (1<= (curY +1) <=8):
    result+=1
if (1<= (curX +2) <=8) and (1<= (curY -1) <=8):
    result+=1
if (1<= (curX +1) <=8) and (1<= (curY +2) <=8):
    result+=1
if (1<= (curX -1) <=8) and (1<= (curY +2) <=8):
    result+=1
if (1<= (curX +1) <=8) and (1<= (curY -2) <=8):
    result+=1
if (1<= (curX -1) <=8) and (1<= (curY -2) <=8):
    result+=1
        
print(result)
