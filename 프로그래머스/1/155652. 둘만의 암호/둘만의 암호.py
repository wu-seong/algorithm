def solution(s, skip, index):
    # a->z까지 문자열을 쓰고
    # skip에 해당하는 걸 지운다
    # 인덱스 만큼 문자열을 뒤로 민다.
    
    alpha_list = list("abcdefghijklmnopqrstuvwxyz")
    for skip_alpha in skip:
        alpha_list.remove(skip_alpha)
    #print(alpha_list)
    result = []
    n = len(alpha_list)
    for a in s:
        find_idx = alpha_list.index(a)
        result.append(alpha_list[(find_idx + index)%n])
    #print(result)
    return "".join(result)
        
    