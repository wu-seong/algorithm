'''
끝에 있는 것 부터 택배 보낼 것 채우고,
끝에 있는 것 부터 수거도 하기
만약 끝에 있는 것 둘 다 0/0 이면 0/0 아닐 때 까지 pop하기
시행 횟수마다 길이 * 2만큼 더하기

누적합으로 뒤에서부터 더하기
첫 
'''
def solution(cap, n, deliveries, pickups):
    if not sum(deliveries) + sum(pickups):
        return 0
    result = 0
    #print(home)
    while deliveries or pickups: # 둘 중 하나라도 작업이 남아있다면 반복
        cur = cap
        move_length = max(len(deliveries), len(pickups))*2
        result += move_length
        while deliveries:# 택배가 남아있으면 반복
            last = deliveries[-1]
            #print(last, cur)
            # 해당 위치에서 작업이 끝난 경우
            if last <= cur:
                deliveries.pop()
                cur -= last
            else: # 일부만 작업한 경우
                deliveries[-1] -= cur
                break
                    
        cur = cap
        while pickups:# 택배가 남아있으면 반복
            last = pickups[-1]
            # 해당 위치에서 작업이 끝난 경우
            if last <= cur:
                pickups.pop()
                cur -= last
            else: # 일부만 작업한 경우
                pickups[-1] -= cur
                break
        #print(deliveries, pickups)
    #print(home)
    return result

    
