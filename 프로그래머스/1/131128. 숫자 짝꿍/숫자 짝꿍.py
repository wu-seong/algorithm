from collections import defaultdict
def solution(X, Y):
    # 각 숫자당 digit 카운팅
    # 각 자리 수당 더 작은 것을 채택
    x_dict, y_dict = defaultdict(int), defaultdict(int)
    for x in X:
        x_dict[int(x)] += 1
    for y in Y:
        y_dict[int(y)] += 1
    
    du_list = [0] * 10
    for i,v in enumerate(du_list):
        du_list[i] = min(x_dict[i], y_dict[i])
    #print(du_list)
    exist = set()
    for i in range(10):
        if du_list[i] != 0:
            exist.add(i)
    if not exist:     # 아무것도 없으면 -1 리턴
        return "-1"
    elif len(exist) == 1 and list(exist)[0] == 0: # 만약 0밖에 없으면 "0" 리턴
        return "0"
    else:    
        # 높은 것부터 문자열에 더하기
        result = ""
        for i in range(9,-1, -1):
            result += str(i)*du_list[i]
    #print(result)
    return result
    