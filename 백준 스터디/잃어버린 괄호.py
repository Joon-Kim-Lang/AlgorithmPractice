iptStr = input()
iptStr = iptStr + ' '

tempStr = ''
result = 0
isMinus = False

for char in iptStr:
  if char.isdigit():
    tempStr = tempStr + char
  
  else:
    #맨 처음 부호로 -가 나올경우
    if tempStr == '':
      tempStr = '0'

    if isMinus:
      result -= int(tempStr)
      tempStr = ''
    else:
      result += int(tempStr)
      tempStr = ''
    
    if char == '-':
      isMinus = True

print(result)