from collections import deque
def solution(n):
    """
    
    """
    dic = {0:"1", 1:"2", 2:"4"}
    r = 1
    n -= 1
    result = dic[n % 3]
    n -= 3
    n = n // 3
    while n >= 0:
        #print(result)
        result = dic[n % 3] + result
        n -= 3
        n = n // 3
    #print(result)
    return result
            