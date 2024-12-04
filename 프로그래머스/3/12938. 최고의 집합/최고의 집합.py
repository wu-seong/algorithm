'''
합이 9이면서 서로의 차이가 가장 적은 것

n = 1일 때는 s 그자체가 최고의 집합
n = 2일 때는 2로 나누어 떨어지면 2로 나눈 몫 나머지는 1더하기
n = 3일 때는 3으로 나누어 떨어지면 2로 나눈 몫 나머지는 1이면 1더하기, 2면 1,1 더하기
'''
def solution(n, s):
    if n == 1: 
        return [s]
    if n > s:
        return [-1]
    q = s//n
    rest = s % n
    
    result = [q] * n
    i = 0
    while rest > 0:
        result[i] += 1
        i += 1
        rest -= 1
    result.sort()
    print(result)
    return result
        
    
    
    

    