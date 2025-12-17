'''
더하기 or 빼기 2가지 선택지
2^20 = 1000 * 1000 = 1,000,000 

더하거나 빼기 둘 중에 하나를 선택하여 깊이가 n에 도달 했을 때 target을 비교하고 카운팅

'''

def solution(numbers, target):
    n = len(numbers)
    memo = {}
    
    def dfs(idx, tmp):
        if idx == n:
            return 1 if tmp == target else 0
        if (idx, tmp) in memo:
            return memo[(idx, tmp)]
        
        result = (dfs(idx + 1, tmp + numbers[idx]) +
                dfs(idx + 1, tmp - numbers[idx]))
        memo[(idx, tmp)] = result
        return result
        
    return dfs(0, 0)
    