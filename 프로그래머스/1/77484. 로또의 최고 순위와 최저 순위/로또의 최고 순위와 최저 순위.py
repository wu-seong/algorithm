def solution(lottos, win_nums):
    # 원래 몇 개 맞았는지 비교
    cnt = 0
    cnt_zero = 0
    for i in range(6):
        if lottos[i] == 0: #훼손된 것 카운팅
            cnt_zero += 1
            continue
        if lottos[i] in win_nums: # 맞은 것 카운팅
            cnt += 1
    # 최저는 + 0 개 최고는 0의 개수만큼
    high = cnt + cnt_zero
    low = cnt
    # 최고, 최저 순위 계산 하여 저장
    h_rank = 7-high
    l_rank = 7-low
    if h_rank == 7: # 0개도 6위
        h_rank = 6
    if l_rank == 7:
        l_rank = 6
    answer = [h_rank, l_rank]
    return answer