from collections import defaultdict

def dfs(num, visited, graph):
    # 컴퓨터 number를 받아서 방문 표시하고 다음 노드 방문
    # 방문하지 않은 노드만 방문
    #print(num, "노드 방문")
    for nxt in graph[num]:
        if not nxt in visited:
            visited.add(nxt)
            dfs(nxt, visited, graph)
    

def solution(n, computers):
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            connect = computers[i][j]
            if connect:
                graph[i].append(j)
                graph[j].append(i)
    print(graph)
    visited = set()
    result = 0
    for i in range(n):
        # 방문하지 않은 노드이면 카운팅하고 dfs
        if i not in visited:
            result += 1
            visited.add(i)
            dfs(i, visited, graph)
    return result
    '''
    그래프 정보를 만들고
    
    0~n-1까지
    dfs하고 dfs 시작할 때 마다 카운팅하기
    
    이미 방문한 노드이면 지나가기
    
    '''
