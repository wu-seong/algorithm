from collections import defaultdict
def solution(topping):
    # multi set으로 생각하고
    # 토핑번호를 key로하여 카운팅
    # 0 : n로 시작해서, 서로 multiset을 만든다.
    m_set1 = defaultdict(int)
    m_set2 = defaultdict(int)
    for t in topping:
        m_set1[t] += 1
    # n-1 : 1이 될 때 까지 토핑을 하나씩 옮긴다.
    # 옮겨진 것이 0이 되면 key에서 지운다
    # 두 딕셔너리의 key 개수를 비교해서 같으면 카운팅
    cnt = 0
    for i in range(len(topping)): # 첫번째 토핑부터 시자해서 마지막 토핑까지 옮긴다.
        t = topping[i]
        m_set1[t] -= 1
        if m_set1[t] == 0:
            m_set1.pop(t, None)
        m_set2[t] += 1
        #print(m_set1, m_set2)
        if len(m_set1) == len(m_set2):
            cnt += 1
    return cnt
            
       