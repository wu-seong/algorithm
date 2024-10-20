def search_str(z_dict, target_str): # 문자열 색인 번호 반환, 없으면 0반환
    for i in range(len(z_dict)):
        if z_dict[i] == target_str:
            return i
    return 0
def solution(msg):
    # 각 글자를 시작으로 가장 긴 문자열에 해당하는 색인번호를 대치
    # 각 입력을 가장 긴 문자열로 압축
    # 해당 길이의 문자열로 압축이 안되면 바로 이전의 압축을 채택
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    z_dict = [''] * (27)
    for i in range(26):
        z_dict[i+1] = alpha[i]

    result = [] # 답
    n = len(msg)
    start = 0
    while start < n:
        end = start + 1
        # 찾을 문자열
        # 최대 end len일 때 까지 
        searched_idx = 0
        while end <= n:
            target_str = msg[start:end]
            # 해당 문자열이 사전에 있는지를 반환
            res = search_str(z_dict, target_str)
            if res: # 있다면 색인번호 기억하기
                searched_idx = res
                end += 1
                if end > n:
                    result.append(searched_idx)
                    return result
            else: # 없으면 기억한 색인번호 추가 및 찾는 문자열 사전에 추가
                result.append(searched_idx)
                z_dict.append(target_str)
                start = end - 1
                break
    print(result)
    return result
        
            
    
    