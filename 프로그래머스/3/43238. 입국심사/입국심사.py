'''
30
4 + 2

m을 각 시간으로 나눈 몫의 합이 n이상이면 그 이상은 버리기
미만이면 아래를 버리기

걸리는 시간이 M초라고 한다면 
M+1초에는 모든 
'''
def solution(n, times):
    start = 1
    end = 1e18
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for t in times:
            sum += (mid // t)
        if sum >= n:
            end = mid - 1
        else:
            start = mid + 1
    print(start, end)
    return start