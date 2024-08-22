def solution(sizes):
    # 곱셈은 몰릴 수록 작아짐
    # 한쪽이 작은 쪽으로 몰기
    min_w = 0
    min_h = 0
    for w,h in sizes:
        if w > h:
            short = h
            long = w
        else:
            short = w
            long = h
        min_w = max(min_w, short)
        min_h = max(min_h, long)
    answer = min_w * min_h
    return answer

