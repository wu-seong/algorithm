def solution(diffs, times, limit):
    '''
    1 ~ max(diffs) 를 이진탐색하면서 계산해서 limit 비교하기
    
    만약 해당 level이 limit보다 크면 오른쪽을 탐색
    limit보다 작거나 같으면 더 작은 왼쪽을 탐색한다.
    
    로그 10만 -> 16 * 30만
    '''
    start = 1
    end = max(diffs)
    n = len(diffs)
    min_level = max(diffs)
    while start <= end:
        mid = (end + start) // 2
        #print(start, end, mid)
        p_sum = 0
        for i in range(n):
            if diffs[i] <= mid: # 바로 풂
                p_sum += times[i]
            else: 
                p_sum += (times[i] + times[i-1]) * (diffs[i] - mid) + times[i]
            #print(p_sum)
        if p_sum <= limit:
            min_level = min(min_level, mid)
            end = mid - 1
        else:
            start = mid + 1
    print(min_level)
    return min_level