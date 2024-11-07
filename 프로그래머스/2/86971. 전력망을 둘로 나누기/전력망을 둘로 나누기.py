from collections import defaultdict
def solution(n, wires):
    '''
    각각의 노드가 가지는 자식 노드의 수를 모두 구하기
    dfs로 순회하면서 리프 노드 = 1
    탐색이 끝나면 반환 값 모두 더해서 본인의 자식 노드 수 저장
    본인 노드 + 자식노드 수가 가장 절반에 가까운 것
    '''
    graph = defaultdict(list)
    visited = set()
    for wire in wires:
        start, end = wire
        graph[start].append(end)
        graph[end].append(start)
    
    '''
    dfs 하면서 돌아올 때 자식 노드의 수 카운팅하기
    '''
    
    node_cnt = [0]*(n+1)
    def dfs(current):
        if len(graph[current]) == 0:
            node_cnt[current] == 1
            return 1
        child_cnt = 0
        for next_node in graph[current]:
            if not next_node in visited:
                visited.add(next_node)
                child_cnt += dfs(next_node)
        node_cnt[current] = child_cnt + 1
        return node_cnt[current]
    visited.add(1)
    dfs(1)
    
    print(node_cnt)
    '''
    골라서 나눴을 때 차이 구해서 최솟값 찾기
    '''
    min_dif = n
    for cnt in node_cnt:
        min_dif = min(min_dif, (abs((n - cnt) - cnt)))
    print(min_dif)
    return min_dif
        
        
    
    
    