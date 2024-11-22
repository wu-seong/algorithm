def solution(cards):
    '''
    8 -> 4 -> 7 -> 1
    2 -> 5 -> 6
    
    여러 숫자 사이클을 구하고
    
    그 중에서 가장 숫자 사이클이 높은 두 사이클의 길이를 곱한다.
    
    만약 사이클 하나로 모두 연결되어 있다면 0
    
    여러 사이클 구하는 법
    
    모든 카드를 선택할 때 까지 반복
    하나의 사이클이 만들어졌다면 사이클 목록에 추가
    
    '''
    n = len(cards)
    visited = set()
    not_visited = set(range(1,n+1))
    print(visited, not_visited)
    cycle = []
    while len(visited) < n:
        current = not_visited.pop()
        temp = set()
        # 방문하지 않은 점 dfs하기
        length = 0
        while True:
            # 현재점 방문하고 
            temp.add(current)
            length += 1
            # 다음 점 체크
            next = cards[current-1]
            # 만약 현재사이클 중 이전에 방문했던 점이면 visited, not_visited 갱신
            if next in temp:
                visited.update(temp)
                not_visited -= temp
                cycle.append(length)
                break
            current = next
    print(cycle)
        
    if len(cycle) == 1:
        return 0
    cycle.sort(reverse=True)
    return cycle[0] * cycle[1]