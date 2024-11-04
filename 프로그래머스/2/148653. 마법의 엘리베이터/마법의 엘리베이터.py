from copy import deepcopy
def solution(storey):
    """
    0층 보다 아래는 없음
    
    
    """
    
    target = list(map(int, str(storey)))
    n = len(target)
    target.insert(0,0)
    result = 0
    
    for i in range(n,-1,-1):
        if 1 <= target[i] < 5:
            result += target[i]
        elif target[i] == 5: # 5는 앞의 숫자에 따라 올릴지 내릴지가 달라진다.
            if target[i-1] >= 5: 
                result += (10 - target[i])
                target[i-1] += 1
            else:
                result += target[i]
        elif 6 <= target[i] < 10:
            result += (10 - target[i])
            target[i-1] += 1
        elif target[i] == 10: # 앞에 것으로 인해서 9 -> 10이됨, 그담 숫자에 반영
            target[i-1] += 1
    #print(result)
    return result
            