def solution(n, lost, reserve):
    # reserve 에서 lost를 제거
    # lost에서도 revserve를 제거
    # lost, reserve 오름차순 정렬
    temp_lost = [num for num in lost]
    lost = set(lost) - set(reserve)
    reserve = set(reserve) - set(temp_lost)
    lost = sorted(lost)
    reserve = sorted(reserve, reverse=True)
    print(lost, reserve)
    
    # lost를 순회하면서 reserve에서 가장 작은 체육복을 pop하기
    cnt = 0
    for lost_num in lost:    
        while reserve and reserve[-1] <= lost_num + 1: # 다 찾았거나, 찾을 가능성이 있는 옷만 탐색
            reserve_num = reserve.pop()
            #print(lost_num, reserve, reserve_num)
            if lost_num -1 == reserve_num or lost_num+1 == reserve_num: # 찾으면 pass
                break
        else: # 못찾으면 카운팅
            cnt += 1
    result = n - cnt
    #print(result)
    return result            
    