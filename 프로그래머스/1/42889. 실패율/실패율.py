def solution(N, stages):
    # 도달 o 클리어 x cnt / 도달 o cnt
    # 스테이지 별로 실패율 구해서 내림차순 정렬 (20만 )
    # 
    # 실패율 구하기
    # stages 순회하면서 각 stage마다 카운팅
    # N+1은 모두 클리어 한거라 제외
    clear_list = [0] * (N+2) #(1~N+1 최종 도달 스테이지)
    for s in stages:
        clear_list[s] += 1
    #print(clear_list)
    # 전체 개수 - 이전 누적 개수 == 도달 개수
    # 도달 o 클리어 x 개수 = 이전 누적 개수
    # 3 2 5 2 3
    result = []
    s_sum = sum(clear_list)
    acc_sum = 0
    for i,cnt in enumerate(clear_list): # clear_list 순회하면서 실패율 구하기
        if i == 0 or i == N+1:
            continue
        if s_sum - acc_sum == 0: # 스테이지에 도달한 유저가 없는 경우
            result.append((i,0))
            continue
        #print(cnt, s_sum, acc_sum)
        rate = cnt/(s_sum - acc_sum)
        acc_sum += cnt
        result.append((i,rate))
    result.sort(reverse=True, key=lambda x: x[1])
    answer = [x[0] for x in result]
    #print(answer)
    return answer
    