from collections import deque
def solution(plans):
    '''
    일단 시간 오름차순으로 정렬
    
    진행할 과제 stack에 넣기
    현재과제가 끝나기 전 시간 안에 다음 과제가 있으면 다음 과제 시작 시간 - 현재 과제 시작시간(남은시간)을
    stack에 넣고 다음 과제를 시작
    
    과제를 완료했으면 해당 시간에 시작하는 과제 있으면 stack에 넣고 stack에서 이전에 넣었던 과제를 마저 수행하기
    
    완료한 과목은 result에 넣기
    
    result의 수가 plans의 길이일 때 까지 반복
    '''
    def transfer(time_str):
        hour, minuet = time_str.split(":")
        return int(hour)*60 + int(minuet)
    n = len(plans)
    
    for plan in plans:
        plan[1] = transfer(plan[1])
        plan[2] = int(plan[2])
    plans.sort(key = lambda x: x[1])

    plans = deque(plans)
    #print(plans)
    stack = []
    result = []
    current = 0
    while len(result) < n:
        #print(plans, stack, result)
        if not stack: # 다음 수행할 과제 넣기
            name, start, playtime = plans.popleft()
            stack.append((name, playtime))
            current = start
        else:
            name, remain = stack.pop()
            if plans:
                n_name, n_start, n_playtime = plans[0]
                if n_start < current + remain: # 중간에 다른 과제를 수행해야하는 경우
                    stack.append((name, current + remain - n_start)) # 하던거 멈추고
                    plans.popleft()
                    stack.append((n_name, n_playtime)) # 새로운 거 하기
                    current = n_start
                else: #과제를 바로 수행할 수 있는 경우
                    #print(name, "완료")
                    result.append(name)
                    current += remain
            else:
                result.append(name)
                #print(name, "완료")
                current += remain
    print(result)
    return result
            
        