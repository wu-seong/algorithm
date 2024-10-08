from collections import defaultdict
def solution(k, tangerine):
    # 완탐 -> 시간초과
    # tangerine 배열에서 서로다른 귤을 6개 뽑는다
    # 각 조합마다 set을 하여 종류의 수를 구한다.
    # 그 중 가장 최솟값을 구한다.
    
    # 그리디
    # 같은 종류의 귤을 카운팅 하여 종류가 적은 귤부터 고르기
    # 크기를 키, 개수를 값으로 하여 딕셔너리에 저장
    # 큰 순서대로 k에서 빼기, 한번 연산할 때 마다 전체 종류에서 줄어 드는 것
    # 남은 수 k가 0보다 작으면 끝남 
    dict = defaultdict(int)
    total_type = 0 
    for num in tangerine: # dict 만들기
        dict[num] += 1
    #print("dict:", dict)
    #print("total_type", total_type)
    cnt_list = []
    for key in dict: # 크기 순 정렬
        cnt_list.append(dict[key])
    cnt_list.sort()
    #print(cnt_list)
    type_cnt = 0
    while True: 
        k -= cnt_list.pop()
        type_cnt += 1
        if k <= 0:
            break
    return type_cnt
    
    
    