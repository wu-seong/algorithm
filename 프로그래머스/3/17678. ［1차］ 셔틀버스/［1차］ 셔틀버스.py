'''
가장 막차를 타야함

16
1시간마다 45명을 태움

가장 늦은 막차에 대기하는 크루가 n명 이상이면 해당 차를 못탐
탈 수 있는 차 중에서 가장 마지막 차를 타야함
시뮬레이션을 돌리면서 탈 수 있는 차인지를 판별하기

timetable을 시간순으로 정렬한다.

버스 시간 마다 timetable에서 가장 먼저온 사람을 pop한다.
pop의 횟수가 n이면 그 차는 탈 수 없는 차이다. -> 마지막 타는 녀석보다 1분 빠르게 타기
pop의 횟수가 n미만이면 그 차는 아직 탈 수 있는 차이다. -> 버스 출발할 때 시간에 타기
'''

from collections import deque
def solution(n, t, m, timetable):
    def translate(time):
        hour, minute = time.split(":")
        return int(hour)*60 + int(minute)
    timetable = deque(sorted((map(translate, timetable))))
    bus_times = []
    time = 540
    for i in range(n): 
        bus_times.append(time)
        time += t
    result = 0
    #print(bus_time)
    #print(timetable)
    for bus_time in bus_times:
        cnt = 0
        # m-1명이 탔을 때 다음녀석도 타려고 한다면 m-1명과 같은 초에 타기
        # 그렇지 않다면 버스가 출발할 때 시간으로 타기
        while timetable and timetable[0] <= bus_time and cnt < m:
            #print(timetable)
            c_time = timetable.popleft()
            cnt += 1
            if cnt == m:
                result = max(result, c_time-1)
            
        if cnt < m: 
            result = max(result, bus_time)
    hour = result//60
    minute = result % 60
    if hour < 10:
        hour = '0' + str(hour)
    else:
        hour = str(hour)
    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute)
    print(hour, ":", minute, sep='')
    return hour + ":" + minute
            
    