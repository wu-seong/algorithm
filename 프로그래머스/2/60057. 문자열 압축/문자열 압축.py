from collections import deque
def solution(s):
    '''
    앞에서 부터 n개씩 잘라야한다
    n개씩 잘라서 배열에 저장하기
    자른 것이 뒤의 배열과 다를 때 까지 반복해서 카운팅
    카운트 + 처음 읽은 것 압축 결과 저장
    다른 것 부터 다시 반복
    '''
    n = len(s)
    
    m_result = n
    for i in range(1, n//2 + 1):
        split_s = []
        for j in range(0, n - i + 1, i): # 문자열 반복해서 배열에 저장   
            split_s.append(s[j:j+i])
        #print(split_s)
        split_s.append(s[(n//i)*i:])
        m = len(split_s)
        result = []
        j = 0
        cnt = 1
        while j+1 < m: # 뒤에 압축할 것이 없을 때 까지
            if split_s[j] == split_s[j+1]: # 같으면 카운팅
                cnt += 1
            else: # 다르면 지금까지 카운팅 했던 것 압축해서 저장
                if cnt > 1:
                    result.append(str(cnt))
                result.append(split_s[j])
                cnt = 1
            j += 1
        if cnt > 1: # 마지막까지 반복된 경우
            result.append(str(cnt))
            result.append(split_s[-1])
        else:
            result.append(split_s[-1])
            
        #print("결과", "".join(result))
        m_result = min(m_result, len("".join(result)))
    print(m_result)
    return m_result