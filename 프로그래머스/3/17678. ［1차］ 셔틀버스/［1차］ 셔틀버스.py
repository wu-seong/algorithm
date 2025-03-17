'''
크루원들의 시간 모두 분으로 통일하기
버스가 도착하는 시간도 통일하기
to min, to str 함수 둘 다 필요

콘이 탈 수 있는 시간 중 가장 늦은 시간을 구하기
-> 현재 버스가 마지막일 때는 무조건 타야함. 마지막으로 탑승한 사람보다 1분 빠르게 도착하기
-> 버스 도착 시간마다 먼저 대기하고 있는 사람 태우기, 그다음 1시간 동안 최대한 태우고 못 타는 사람은 대기열에 두기
-> 마지막 버스의 마지막 승객이 되야 하는데, 마지막 버스의 마지막 승객이 도착한 사람의 시간을 구하고 1분 더 빠르게 도착하기
'''

from collections import deque
def solution(n, t, m, timetable):
    def to_min(time):
        hour, min_num = map(int, time.split(':'))
        #print(hour*60 + min_num,'분')
        return hour*60 + min_num
    def to_str(min_num):
        hour = str(min_num//60)
        min_str = str(min_num % 60)
        hour = hour.rjust(2,'0')
        min_str = min_str.rjust(2,'0')
        #print(hour+':' + min_str)
        return hour+ ':' + min_str
    # 타임테이블 변환
    timetable = [to_min(s) for s in timetable]
    timetable.sort(reverse=True)
    #print(timetable)
    #to_str(to_min(timetable[0]))
    wating = deque()
    # 버스 시간 만들기
    bus = [ 540 + t*i for i in range(n)]
    #print(bus)
    # 버스 태우기 시뮬
    last = 0
    result = 0
    for i, b in enumerate(bus):
        # 대기열에 있는 얘들 태우기, 최대 인원까지만
        cur = 0
        while wating and cur < m:
            last = wating.popleft()
            cur += 1
        # timetable얘들 태우기
        while cur < m and timetable and timetable[-1] <= b:
            #print(timetable)
            last = timetable.pop()
            cur += 1
        # 남는 얘들 대기열에 넣기
        while timetable and timetable[-1] <= b:
            wating.append(timetable.pop())
        # 막차일 때
        if i == n-1: 
            # 다 찼으면 마지막 탄얘보다 앞
            if cur == m:
                result = last-1
            # 안찼으면 막차 출발 시간
            else:
                result = b
    #print(to_str(result))
    return(to_str(result))
                
                
'''
good:
필요한 작업 미리 파악해서 함수화 해두기
bad:
디버깅이 오래걸림, 너무 머릿속으로 생각하지 말고 그냥 직접 로그 찍어보는게 빠름. 어디에 어떤 로그를 찍을 지를 고민해서 확실하게 로직을 검증하기
'''
        
        
    