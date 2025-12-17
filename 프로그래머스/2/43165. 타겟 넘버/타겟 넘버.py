'''
더하기 or 빼기 2가지 선택지
2^20 = 1000 * 1000 = 1,000,000 

더하거나 빼기 둘 중에 하나를 선택하여 깊이가 n에 도달 했을 때 target을 비교하고 카운팅

'''

def dfs(max_depth, cur_depth, numbers, tmp, target):
    if max_depth == cur_depth:
        return 1 if tmp == target else 0
        
    return dfs(max_depth, cur_depth + 1, numbers, tmp + numbers[cur_depth], target) + dfs(max_depth, cur_depth + 1, numbers, tmp - numbers[cur_depth], target)

def solution(numbers, target):
    n = len(numbers)
    return dfs(n, 0, numbers, 0, target)
    