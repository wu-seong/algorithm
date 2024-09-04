from collections import defaultdict
def make_comb(menu_list, start, target_level, comb_menu, comb_list):
    if len(comb_menu) == target_level:
        if not comb_menu in comb_list:
            comb_list.append(comb_menu)
        return
    for i in range(start, len(menu_list)):
        make_comb(menu_list, i+1, target_level, comb_menu + menu_list[i], comb_list)
    
def each_coure(orders, num, result):
    comb_list = [] # 각 레벨별 코스 조합을 저장
    count_comb = defaultdict(int) # 코스 조합 주문 횟수를 저장
    # 메뉴 리스트로 레벨 별 조합 만들기
    for order in orders:
        make_comb(order, 0, num, "", comb_list)
    max_count = 0
    max_comb = []
    for order in orders:  # orders에서 각 조합이 포함된 횟수를 카운팅
        for comb in comb_list: 
            contain = True
            for menu in comb: # 모든 메뉴가 order안에 있는지 체크
                if not menu in order:
                    contain = False
                    break
            if contain:
                count_comb[comb] += 1
    for comb in count_comb: # 카운팅 한 것 중 최댓값들 배열에 넣기
        if count_comb[comb] > max_count:
            max_count = count_comb[comb]
            max_comb = []
            max_comb.append(comb)
        elif count_comb[comb] == max_count:
            max_comb.append(comb)
    #print("max comb:",max_comb)
    if max_count >= 2:
        result += max_comb
        
menu_list = []
def solution(orders, course):
    for i in range(len(orders)):
        orders[i] = ''.join(sorted(orders[i]))
    # 메뉴 리스트 저장하기
    for order in orders:
        for menu in order:
            if not menu in menu_list:
                menu_list.append(menu)
        
    answer = []
    for c in course:
        each_coure(orders, c, answer)
    # 코스 요리 오름차순 정렬하기
    for i in range(len(answer)):
        answer[i] = ''.join(sorted(answer[i]))
    answer.sort()
    #print(answer)
    return answer

