'''
제재 가능한 아이디의 경우의 수를 구하기

같은 제제 아이디는 여러개가 있을 수도 있음(가린 곳이 서로 다른)

글자 수 체크
별이 아닌글자가 같은지 체크
같으면 목록에 넣기

모두 목록 구했으면 크기 순으로 정렬
1개인거 먼저 다른 목록에서 제거
또 1개인거 있으면 목록에서 제거

작은것 부터 뽑기?
뽑은건 뒤에서 못 뽑음

'''

def solution(user_id, banned_id):
    n = len(banned_id)
    possible_list = [[] for _ in range(n)]
    for i, b_id in enumerate(banned_id):
        for u_id in user_id:
            if len(u_id) != len(b_id):
                continue
            same = True
            for j in range(len(b_id)):
                if b_id[j] == '*':
                    continue
                if b_id[j] != u_id[j]:
                    same = False
            if same:
                possible_list[i].append(u_id)
    
    possible_list.sort(key=lambda x: len(x))
    print(possible_list)
    
    
    result = 0
    result_set = set()
    def dfs(level, select_set):
        nonlocal result
        nonlocal result_set
        # 끝에 다다르면 카운팅
        #print(level, select_set)
        if level == n:
            if not frozenset(select_set) in result_set:
                result_set.add(frozenset(select_set))
            return
        # 현재것 선택 리스트에 넣기
        for i in range(len(possible_list[level])):
            if not possible_list[level][i] in select_set:
                select_set.add(possible_list[level][i])
                # 다음것 호출
                dfs(level+1, select_set)
                select_set.remove(possible_list[level][i])
    dfs(0, set([]))
    print(result_set, len(result_set))
    return len(result_set)
            