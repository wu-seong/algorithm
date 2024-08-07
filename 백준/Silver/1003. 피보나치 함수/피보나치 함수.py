testCnt = int(input())    
fibo = []
fibo.append(1)
fibo.append(1)
for i in range(2,40):
    fibo.append(fibo[-1] + fibo[-2])
## print(fibo)
result = ''
for i in range(testCnt):
    num = int(input())
    if num == 0 :
        result += '1 0'
    elif num == 1:
        result += '0 1'
    else:
        result +=str(fibo[num-2]) + ' ' + str(fibo[num-1])
    result += '\n'
print(result)