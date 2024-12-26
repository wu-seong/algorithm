'''
판매원과 추천인 정보를 통해
트리 정보를 구축, 자신의 자식 정보를 배열에 가지기

각 판매 수익 통계 중에서 리프노드부터 루프 노드로 올라가기
enroll의 역순으로 판매 정보를 정렬하기
seller 마다의 index를 저장하기

두 seller에서 enroll의 index를 비교해서
더 뒤에 있는 것이 앞에 오도록(내림차순)

그 다음 판매가의 100퍼를 저장, 
본인의 자식에 대한 9분의 1을 추가로 더함
그 다음 총 수입의 90퍼센트만 남기기 1원 미만은 절삭

--- 수정 ---
판매 건수 마다 절삭하는 시점이 달라지기 때문에 각각의 건수로 접근해야한다.
각 건수 마다 부모에게 분배금 지급

'''
from collections import defaultdict
def solution(enroll, referral, seller, amount):
    n = len(enroll)
    index = defaultdict(int)
    for i, v in enumerate(enroll):
        index[v] = i
    #print(index)
    parents = defaultdict(str)
    for i in range(n):
        parent, child = referral[i], enroll[i]
        parents[child] = parent
    #print(parents)
    sell = list(zip(seller, amount))
    #print(sell)
    result = defaultdict(int)
    for seller, amount in sell:
        income = amount * 100
        result[seller] += income
        child = seller
        income *= 0.1
        while income >= 1:
            #print(income, seller)
            parent = parents[child]
            result[parent] += income
            result[child] -= income
            income = int(income*0.1)
            child = parent
    #print(result)
    answer = []
    for name in enroll:
        answer.append(result[name])
    #print(answer)
    return answer
            
        
    