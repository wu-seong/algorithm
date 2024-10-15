def solution(s):
    # 문자열 파싱해서 set 배열로 만들기
    set_list = []
    s = s[2:-2]
    s = s.split("},{")
    for p_s in s:
        p_set = set(map(int, p_s.split(",") ) )
        #print(p_set)
        set_list.append(p_set)
    
    # set길이로 오름차순 정렬
    set_list.sort(key=lambda x: len(x))
    
    # 1개는 먼저 넣기
    value = set_list[0].pop()
    result = [value]
    set_list[0].add(value)
    
    # 이전과 set 차집합 연산 하여 원소 1개 얻기
    for i in range(1,len(set_list)): 
        d_set = set_list[i]-set_list[i-1]
        result.append(d_set.pop())
    #print(result)
    return result
   