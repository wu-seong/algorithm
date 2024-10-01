def solution(n):
    # 각 수 마다 시작점으로 해서 n이 넘어가면 다음 수를 시작점으로
    cnt = 1
    for i in range(1,(n//2)+1):
        sum = 0
        while sum < n:
            sum += i
            if sum == n:
                cnt += 1
                break
            i += 1
    return(cnt)