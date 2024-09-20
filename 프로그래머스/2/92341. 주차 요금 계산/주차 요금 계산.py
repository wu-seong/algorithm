import math
from collections import defaultdict
def solution(fees, records):
    b_min, b_fee, e_min, e_fee = fees
    # 각 차량 번호 별로 순서대로 저장(시간별로 오름차순임)
    parks = defaultdict(list)
    for r in records:
        t,id,p = r.split(" ")
        hour, min = t.split(":")
        min = int(min) + 60*(int(hour))
        parks[id].append(min)
    for id in parks: # 마지막에 출차 정보 없으면 추가
        if len(parks[id]) % 2 != 0:
            parks[id].append( (60*24) -1 ) 
    
    #print(parks)
    # 각 차량별로 요금 정보 계산 
    result = [-1] * 10000
    for id in parks:
        total_min = 0
        for i in range(1,len(parks[id]),2):
            total_min += (parks[id][i] - parks[id][i-1])
            #print(total_min, b_min)
        if total_min > b_min:
            total_fee = b_fee + (math.ceil((total_min - b_min)/e_min) * e_fee)
        else:
            total_fee = b_fee
        result[int(id)] = total_fee
    answer = []
    for r in result:
        if r >= 0:
            answer.append(r)
        #print(answer)
    return answer