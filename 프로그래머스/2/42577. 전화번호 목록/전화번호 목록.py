'''
특정 번호 전체가 다른 번호의 시작에 포함되어 있으면 접두어임 -> false
하나하나 비교 => n^2 시간초과

길이가 작은 것 부터 set에 넣기
포함 여부만 판단 해서 안에 있으면 false
끝까지 없으면 true

'''
def solution(phone_book):
    p_set = set()
    # 정렬
    phone_book.sort(key=lambda x: len(x))
    #print(phone_book)
    for i, s in enumerate(phone_book):
        for j in range(len(s)):
            #print(s[:j+1])
            if s[:j+1] in p_set:
                return False
        p_set.add(s)
        #print(p_set)
    return True