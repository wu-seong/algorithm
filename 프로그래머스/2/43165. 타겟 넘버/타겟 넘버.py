'''
더하기 or 빼기 2가지 선택지
2^20 = 1000 * 1000 = 1,000,000 

더하거나 빼기 둘 중에 하나를 선택하여 깊이가 n에 도달 했을 때 target을 비교하고 카운팅

'''

cnt = 0

def dfs(max_depth, cur_depth, numbers, tmp, target):
    global cnt
    if max_depth == cur_depth:
        #print(tmp)
        if tmp == target:
            cnt += 1
        return
    dfs(max_depth, cur_depth + 1, numbers, tmp + numbers[cur_depth], target)
    dfs(max_depth, cur_depth + 1, numbers, tmp - numbers[cur_depth], target)

def solution(numbers, target):
    global cnt
    n = len(numbers)
    dfs(n, 0, numbers, 0, target)
    #print("총 도달 카운트", cnt)
    return cnt