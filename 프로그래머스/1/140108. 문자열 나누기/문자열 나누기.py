def solution(s):
    # 첫번째 읽은 문자를 저장 및 카운팅을 1로 set
    # 이후에 나온 문자를 첫번째 문자 or 아닌 문자로 구분해서 카운팅
    # 아닌 문자의 수가 첫번째 문자의 수와 같으면 +1하고 한 사이클 끝
    
    # 더이상 읽을 글자가 없을 시에 카운팅하고 종료
    i = 0
    result = 0
    while i < len(s):
        first_alpha = s[i]
        first_cnt = 1
        other_cnt = 0
        i += 1
        while first_cnt != other_cnt and i < len(s): #
            if s[i] == first_alpha:
                first_cnt += 1
            else:
                other_cnt += 1
            i += 1
        result += 1
    #print(result)
    return result
                
      