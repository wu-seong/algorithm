from collections import defaultdict
def solution(keymap, targets):
    # 키는 100개 키당 무작위 여러개, 문자 중복도 가능
    # 최소 키를 눌러야 하는 횟수
    
    # 각 문자당 가장 빠른 횟수를 저장
    # 나오는 순서를 비교해서 더 작은 것을 딕셔너리에 저장
    order = defaultdict()
    for key in keymap:
        for i in range(len(key)):
            alpha = key[i]
            if not alpha in order or i+1 < order[alpha]: # 문자가 key에 없거나 값이 더 작으면 갱신
                order[alpha] = i+1
    #print(order)
    
    # target을 순회하면서 딕셔너리에서 꺼내서 카운팅
    # 만약 key에 존재하지않으면 -1
    result = []
    for target in targets:
        cnt = 0
        for target_alpha in target:
            if not target_alpha in order:
                result.append(-1)
                break
            cnt += order[target_alpha]
        else:
            result.append(cnt)
    #print(result)
    return result