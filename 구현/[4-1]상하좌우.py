N = int(input())
directions = input().split()

X_cor = 1
Y_cor = 1

for i in directions:
    if i == "L":
        if X_cor != 1:
            X_cor -= 1
    elif i == "R":
        if X_cor != N:
            X_cor += 1
    elif i == "U":
        if Y_cor != 1:
            Y_cor -= 1
    elif i == "D":
        if Y_cor != N:
            Y_cor += 1
            
print(Y_cor, X_cor)
