'''
각 기능이 어떻게 동작하는지를 정의
next: pos + 10을 함, 만약 + 10이 video_len >= 이면 video_len로 pos = vidie_len
prev: pos - 10을 함, 만약 - 10이 <= 0 이면 pos = 0 
현재 pos가 오프닝 구간이 내면 오프닝 구간만큼은 건너뛴 다음에 역할 수행
역할 수행 후에도 오프닝 구간이면 다시 건너뛰기
'''
def solution(video_len, pos, op_start, op_end, commands):
    def transform(time_str):
        m,s = map(int, time_str.split(':'))
        return m * 60 + s
    video_len = transform(video_len)
    pos = transform(pos)
    op_start = transform(op_start)
    op_end = transform(op_end)
    print(video_len)
    def skip(pos):
        if op_start <= pos <= op_end:
            pos = op_end
            return pos
        return pos
            
    def next(pos):
        pos = skip(pos)
        if pos + 10 >= video_len:
            pos = video_len
        else:
            pos = pos + 10
        pos = skip(pos)
        return pos
    def prev(pos):
        pos = skip(pos)
        if pos - 10 <= 0:
            pos = 0
        else:
            pos = pos - 10
        pos = skip(pos)
        return pos
    def to_str(time_num):
        m = str(time_num // 60)
        s = str(time_num % 60)
        if len(m) == 1:
            m = '0' + m
        if len(s) == 1:
            s = '0' + s
        return m + ':' + s
        
    for c in commands:
        print(pos)
        if c == 'next':
            pos = next(pos)
        else:
            pos = prev(pos)
    pos = to_str(pos)
    print(pos)
    return pos
    
    