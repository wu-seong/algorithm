from collections import defaultdict

def solution(want, number, discount):
    # 10일 연속으로 종류, 수량이 일치해야 함
    # 완탐 10만 * 조건 확인 10 = 100만
    
    # 10일동안 모두 구할 수 있다면 카운팅, 
    # 첫 10일은 구하고 그 다음은 이전 수량 목록을 이용
    # 새로운 것 추가하고 가장 오래된 것 버리기
    
    # 목표 수량
    target_dict = defaultdict(int)
    for w,n in zip(want,number):
        target_dict[w] = n
    # 결과 카운팅
    cnt = 0
    # dict로 비교
    dict = defaultdict(int)
    for t in discount[:10]:
        dict[t] += 1
    correct = True
    for key in dict: # 하나라도 일치하지 않으면 False
        if target_dict[key] != dict[key]:
            correct = False
            break
    if correct: # 모두 일치해야 카운팅
        cnt += 1
    for i in range(10,len(discount)):
        dict[discount[i]] += 1
        dict[discount[i-10]] -= 1
        correct = True
        for key in dict: # 하나라도 일치하지 않으면 False
            if target_dict[key] != dict[key]:
                correct = False
                break
        if correct: # 모두 일치해야 카운팅
            cnt += 1
    return cnt
        
        
        
        