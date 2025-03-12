
'''
소수를 구할 필요가 없는 거였음
그냥 3 * 10000 * 5000
'''
def solution(begin, end):
    result = []
    for num in range(begin, end+1):
        temp = 1
        if num == 1:
            result.append(0)
            continue
        for i in range(2,int(num**(0.5))+ 1):
            if num % i == 0:
                if num//i <= 10**7: # 몫(표지판)이 1000만 이하이면 
                    temp = num//i
                    break
                temp = i
        result.append(temp)
    
    print(result)
    return result
    
    
    