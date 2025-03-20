'''
최소 1~8명의 응모자가 있음. 각 아이디 길이도 1~8임, alnum으로만 구성, 중복 없음

밴 아이디 개수는 최소 1~n임, 항상 *을 하나이상 포함한다. 최소 1개 이상의 아이디와 매핑됨
밴 리스트는 순서와는 관계가 없다.

각 밴 아이디가 가능한 유저 아이디가 몇 개인지를 구해서 곱하기
근데 순서가 없기 때문에 만약 임의의 아이디를 구했다면 제외시켜야 함

각 아이디마다 가능한 매칭 목록을 모두 구하기
적은 것 순서대로 매칭을 먼저 했는데 남은 것이 없을 수가 있나?
dfs로 고르기
40 40 16000000

bcd
bca
**a
bc*
적은 순서대로 한다고 해도 항상 옳은 매칭을 하는 것은 아님
그러니까 결국 선택하고 끝까지 가서 모두 매칭이 가능한지를 확인해봐야하는 것임
근데 이제 순서는 중요하지 않으니까 그냥 밴 리스트에 담긴 순서대로 가능한 리스트를 선택하면 됨

1. 각 밴 id가 가능한 유저 아이디 목록을 구한다.
2. 밴 리스트 순서대로 가능한 목록 중 1개씩 선택해서 중복 선택이 없이 끝까지 가는 경우를 찾고 카운팅
백트래킹인거지 

각 userid 마다 해당 별 위치에 별을 넣어서 같으면 리스트에 넣기

'''
def solution(user_id, banned_id):
    def get_star_index(bid):
        temp = []
        for i, c in enumerate(bid):
            if bid[i] == '*':
                temp.append(i)
        return temp
    def is_possible(uid, bid):
        uid = list(uid)
        # 길이 확인
        if len(uid) != len(bid):
            return False
        # 문자 확인
        star_index_list = get_star_index(bid)
        # 변환
        for index in star_index_list:
            uid[index] = '*'
        # 비교
        if uid == list(bid):
            return True
        return False
    n,m = len(user_id), len(banned_id)
    p_list = [ [] for _ in range(m)]
    # 각 밴 아이디 매칭 가능한 유저 리스트 구하기
    for i, bid in enumerate(banned_id):
        for uid in user_id:
            if is_possible(uid, bid):
                p_list[i].append(uid)
    #print(p_list)
    
    result = 0
    '''
    하나씩 선택하고, 선택한 목록을 set으로 갖고 있기
    선택한 것을 제외해서 선택하고 level이 m 까지 간다면 + 1한다.
    '''
    #1~m
    result_set = set()
    def dfs(depth, selected):
        nonlocal result_set
        # 하나씩 선택하기
        if depth == m:
            #print('도달된 목록',selected)
            result_set.add(frozenset(selected))
            return
        for pid in p_list[depth]:
            if not pid in selected:
                selected.add(pid)   
                dfs(depth+1, selected)
                selected.remove(pid)
    dfs(0, set())
    #print(result_set)
    return len(result_set)
            
            
        
 