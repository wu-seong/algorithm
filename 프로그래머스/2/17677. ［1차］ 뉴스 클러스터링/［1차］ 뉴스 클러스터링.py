'''
다중 집합에서 교집합, 합집합 구하기
딕셔너리를 이용해서 key: 개수 저장하기

교집합: key가 겹치고, 둘 중 최솟값
합집합: key가 겹치지 않으면 해당 값, 겹친다면 둘 중 최댓값
'''
def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    m_set1, m_set2 = dict(), dict()
    # 다중집합 만들기
    for i in range(len(str1)-1):
        s = str1[i:i+2]
        if not s.isalpha():
            continue
        if not s in m_set1:
            m_set1[s] = 1
        else:
            m_set1[s] += 1
    for i in range(len(str2)-1):
        s = str2[i:i+2]
        if not s.isalpha():
            continue
        if not s in m_set2:
            m_set2[s] = 1
        else:
            m_set2[s] += 1
    #print(m_set1, m_set2)
    def intersection(a,b):
        temp = dict()
        for k1 in a:
            if k1 in b:
                temp[k1] = min(a[k1], b[k1])
        return temp
    def union(a,b):
        temp = dict()
        for k1 in a:
            if k1 in b:
                temp[k1] = max(a[k1], b[k1])
            else:
                temp[k1] = a[k1]
        for k2 in b:
            if not k2 in a:
                temp[k2] = b[k2]
        return temp
    
                
    i_set = intersection(m_set1, m_set2)
    u_set = union(m_set1, m_set2)
    #print(i_set, u_set)
    i_sum, u_sum = 0, 0
    for key in i_set:
        i_sum += i_set[key]
    for key in u_set:
        u_sum += u_set[key]
    #print(i_sum, u_sum)
    if u_sum:
        print(i_sum/u_sum)
        return int(i_sum/u_sum*65536)
    else:
        return 65536
                
        
        
