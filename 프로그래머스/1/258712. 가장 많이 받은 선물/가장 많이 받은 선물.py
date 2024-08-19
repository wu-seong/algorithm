
def solution(friends, gifts):
    answer = 0
    gift_table = {}
    for s in friends: # 초기화
        gift_table[s] = {}
        gift_table[s]['g1'] = 0
        for r in friends:
            gift_table[s][r] = 0

    for gift in gifts:
        s,r = gift.split(" ")
        # 준 선물 횟수 계산
        gift_table[s][r] += 1
        # 선물 지수 계산
        gift_table[s]['g1'] += 1
        gift_table[r]['g1'] -= 1
    print(gift_table)
    next = {key: 0 for key in friends}
    max_cnt = 0
    for i in range(len(friends)):
        s = friends[i]
        for j in range(i):
            r = friends[j]    
            if gift_table[s][r] > gift_table[r][s]: 
                next[s] += 1
            elif gift_table[s][r] < gift_table[r][s]:
                next[r] += 1
            else:
                if gift_table[s]['g1'] > gift_table[r]['g1']:
                    next[s] += 1
                elif gift_table[s]['g1'] < gift_table[r]['g1']:
                    next[r] += 1
            max_cnt = max(max_cnt, next[s], next[r])

    print(max_cnt)
    # 각 사람 마다 어떤 친구에게 몇번 줬는지 2차원 딕셔너리로 저장
    # 선물지수도 동시에 계산
    # 각 사람 마다 친구에게 준 선물과 친구에게 받은 선물 갯수를 비교하여
    # 다음번에 선물 받을 사람을 정하고 cnt + 1
    # 개수가 똑같다면 선물 지수 비교
    # 지수도 똑같다면 cnt하지 않음
    return (max_cnt)