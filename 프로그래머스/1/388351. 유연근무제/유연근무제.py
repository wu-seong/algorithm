'''
직원 최대 1000명
i번째 직원이요일에 j일차에

schedule에서 + 10을 해서 시간에 반영

각 요일 마다 schedule 시간보다 하나라도 크다면 제외임(주말 제외)

weekdend = []
startday + j == 6 or 7 이면 제외
'''

def check(sch, times, sday):
    cnt = 0
    for i in range(n):
        for j in range(7):
            if sday + j == 6 or sday + j == 7 or sday + j == 13:
                continue
            if sch[i] < times[i][j]:
                cnt += 1
                break
    return cnt
def set_time(schedules):
    for i, t in enumerate(schedules):
        temp = t + 10
        if temp % 100 >= 60:
            temp += 40
        schedules[i] = temp
    
n = 0
def solution(schedules, timelogs, startday):
    global n
    n = len(schedules)
    set_time(schedules)
    fail_cnt = check(schedules, timelogs, startday)
    return n - fail_cnt
    
   