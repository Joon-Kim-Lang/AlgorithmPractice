from itertools import combinations
import copy
N, M  = map(int,input().split())

cityMap = []
for i in range(N):
  cityMap.append(list(map(int, input().split())))


def cityChikDistCalculate(cityChicken,cityHouse):
  cityChikDist = 0

  for i in range(len(cityHouse)):
    chikDist = 9999999
    for j in range(len(cityChicken)):
      tempChikDist = abs(cityHouse[i][0] - cityChicken[j][0])+ abs(cityHouse[i][1] - cityChicken[j][1])
      if tempChikDist < chikDist:
        chikDist = tempChikDist
      if j == len(cityChicken) -1:
        cityChikDist += chikDist 

  return cityChikDist

cityHouse = []
cityChicken = []

for i in range(N):
  for j in range(N):
    if cityMap[i][j] == 1:
      cityHouse.append([i,j])
    elif cityMap[i][j] == 2:
      cityChicken.append([i,j])

#콤비네이션 구현
if len(cityChicken) -M == 0:
  print(cityChikDistCalculate(cityChicken,cityHouse))

else:
  comList = []
  for i in range(len(cityChicken)):
    comList.append(i)

  comList = list(combinations(comList,len(cityChicken) -M))

  minChikDist = 9999999
  copiedCityChicken = copy.deepcopy(cityChicken)
  for i in comList:
    tempArray = []    
    for j in range(len(i)):
      tempChiKFc = copiedCityChicken[i[j]]
      tempArray.append(tempChiKFc)
      cityChicken.remove(tempChiKFc)
      if j == len(i)-1:
        tempChikDist = cityChikDistCalculate(cityChicken,cityHouse)
        if tempChikDist < minChikDist:
          minChikDist = tempChikDist
        for k in tempArray:
          cityChicken.append(k)
  print(minChikDist)

            
    
