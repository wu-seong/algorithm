def solution(msg):
    # 각 글자를 시작으로 가장 긴 문자열에 해당하는 색인번호를 대치
    # 1000 * 1000 = 1,000,000
    # 영문 사전 초기화
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    z_dict = [""]*27 # 리스트 저장
    for i in range(26):
        z_dict[i+1] = alpha[i]
    #print(z_dict)
    # 각 글자가 사전에 있는지를 확인
    # 사전에 없을 때 까지 한글자씩 늘리기
    # 없을 때를 찾으면 없는 것을 사전에 추가하고(w+c)
    # 없을 때의 직전 색인번호를 결과에 추가(w)
    result = []
    n = len(msg)
    start = 0
    idx = 26
    while start < n: # 모든 문자를 다 치환할 때 까지
        # 사전을 순회하면서 만약 있다면 그 색인번호를 저장하고 break
        # 그 다음 길이를 탐색, 없다면 찾는 문자열을 사전에 추가
        end = start + 1
        searched_idx = 0 #이전에 찾은 문자
        while True: # 다 탐색하거나, 없을 때 까지 반복            
            search_str = msg[start:end] # 문자열 갱신
            fail = True
            #print("search_str", search_str)
            for i in range(len(z_dict)): # 찾기
                if search_str == z_dict[i] :
                    searched_idx = i
                    fail = False
                    break
            end += 1
            if fail : # 찾는 것에 실패할 때
                z_dict.append(search_str)
                result.append(searched_idx)
                start = end - 2
                #print("next", result, start)
                break
            elif end > n: # 나머지 문자열이 사전안에 다 있을 때
                result.append(searched_idx)
                start = end
                break
    #print(result)
    return result
        
            
    
    