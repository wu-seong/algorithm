from collections import deque
def solution(bandage, health, attacks):
    '''
    붕대 감기를 시뮬레이션 하기
    
    초 당 시뮬레이션 돌리면서 붕대를 감기
    초에 적의 공격이 있으면 붕대를 감지 않고 체력 소모
    만약 체력이 0 이하가 된다면 -1을 리턴
    
    공격이 모두 끝날 때 까지 버티면 남은 체력을 리턴 
    '''
    
    attacks = deque(attacks)
    max_health = health
    t = 0
    b_stack = 0
    need_time, r_per, r_extra = bandage
    while attacks:
        t += 1
        # 공격이 있으면 공격당하기
            # 공격 당한 체력이 0 이하이면 끝
            # 붕대 스택 초기화하기
        if t == attacks[0][0]:
            time, damage = attacks.popleft()
            health -= damage
            if health <= 0:
                return -1
            b_stack = 0
        else:
        # 붕대 감기
            health = min(max_health, r_per + health)
            b_stack += 1
            if b_stack == need_time: # 스킬 시전 시 쿨타임 초기화
                health = min(max_health, r_extra + health)
                b_stack = 0
    print(health)
    return health