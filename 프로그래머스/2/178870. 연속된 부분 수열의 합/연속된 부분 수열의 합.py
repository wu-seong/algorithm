def solution(sequence, k):
    # start index와 end index를 범위를 조절하며 k가 되면 인덱스를 저장
    
    # 현재까지의 합이 k보다 작으면 end_index를 계속 늘린다.
    # 현재의 합이 k보다 커지면 start index를 늘린다.
    
    # 그러다 k가 되면 시작인덱스와 끝 인덱스를 저장
    # 하고 end_index를 늘린다.
    
    # end_index가 마지막이되면
    # 합이 만약 k보다 작으면 끝내고
    # 합이 만약 k보다 크면 start_index를 계속 늘려서 end index보다 커지면 종료시킨다.
    start = 0
    end = 0
    n = len(sequence)
    result = []
    sum = sequence[0]
    while start <= end: # 계속 줄여서 start > end이면 현재까지 구한 것이 가장 최적인 것
        #print(start,end, sum)
        if sum == k: # 같으면 저장
            if not result or (end-start != result[1] - result[0]): # 같은 값이면 갱신 x
                result = [start,end]
        if sum < k: # 작으면 늘려서 더 최적값 탐색
            if end == n-1: # 더 늘릴 수 없으면 끝
                return result
            end += 1
            sum += sequence[end]
        else: # 크거나 같으면 줄이기 
            sum -= sequence[start]
            start += 1 
    return result