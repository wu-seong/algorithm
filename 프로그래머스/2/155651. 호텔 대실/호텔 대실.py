from collections import defaultdict
def solution(book_time):
    '''
    필요한 최소 객실 수
    -> 동시에 객실을 이용하는 최대 개수
    이용 시작 시 + 1, 이용 종료 시 + 10분에 -1
    
    각 시간 마다 시작시간, 종료시간을 저장
    1분씩 체크하면서 최대 동시 이용 수를 갱신
    '''
    
    '''
    각 book time을 돌면서 분당 start 와 end를 카운팅
    '''
    start_per_min, end_per_min = defaultdict(int), defaultdict(int)
    
    def transfer_minuet(time_str):
        hour, minuet = int(time_str[:2]), int(time_str[3:5])
        minuet += hour * 60
        return minuet
    transfer_minuet(book_time[0][0])
    for start, end in book_time:
        start_minuet = transfer_minuet(start)
        end_minuet = transfer_minuet(end) + 10
        start_per_min[start_minuet] += 1
        end_per_min[end_minuet] += 1
    # print(start_per_min)
    # print(end_per_min)
    
    '''
    시간을 0부터 1씩 올려서 1440까지 각 수에 start는 +하고 end는 -함
    '''
    cnt = 0
    max_cnt = cnt
    for i in range(1440):
        cnt += start_per_min[i]
        cnt -= end_per_min[i]
        max_cnt = max(max_cnt, cnt)
    return max_cnt