from collections import defaultdict
def solution(str1, str2):
    # 두 글자씩 끊어 원소로 만들기
    # 영문자 아니면 버리기 (isAlpha)
    # 모두 소문자로 만들기 (lower)
    # 튜플에 저장 및 카운팅
    #print(str1, str2)
    key1 = []
    for i in range(len(str1)-1):
        p_str = str1[i:i+2]
        if p_str.isalpha():
            key1.append(p_str.lower())
    key2 = []
    for i in range(len(str2)-1):
        p_str = str2[i:i+2]
        if p_str.isalpha():
            key2.append(p_str.lower())
    if not key1 and not key2:
        return 65536
    #print(key1, key2)
    A = defaultdict(int)
    B = defaultdict(int)
    for key in key1:
        A[key] += 1
    for key in key2:
        B[key] += 1
    #print(A,B)
    # 교집합 구하기
    # B에 A와 같은 키가 있으면 min(A[key], B[key]) 하여 카운팅 합산이 교집합
    du_cnt = 0
    
    for key in A:
        if key in B:
            du_cnt += min(A[key],B[key])
    # 합집합 구하기
    # 둘다 카운팅 - 교집합
    sum_cnt = 0
    for key in A:
        sum_cnt += A[key]
    for key in B:
        sum_cnt += B[key]
    sum_cnt -= du_cnt
    #print(du_cnt/sum_cnt)
    return int(du_cnt/sum_cnt*65536)
        