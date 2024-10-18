def solution(n, m, section):
    # 0~n-1까지 순회하면서 section-1 이면 i~i+m까지(i+m <n) 건너뛰고 카운팅
    # -> section을 순회하면서 마지막 원소를 확인하면서 첫번째 것 + m보다 작은 것까지 popleft
    
    i = 0
    cnt = 0
    s_len = len(section)
    while i < s_len:
        start = section[i] 
        cnt += 1
        while i < s_len and section[i] < start+m:
            i += 1    
    #print(i, cnt)
    return cnt
            
        