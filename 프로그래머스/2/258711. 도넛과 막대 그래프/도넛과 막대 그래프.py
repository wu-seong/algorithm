import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
def dfs(graph, visited, current, answer):
    # 끊기면 막대
    if not graph[current]:
        answer[2] += 1
        return
    # 재방문한 곳의 엣지가 1이면 도넛
    if visited[current]:
        answer[1] += 1
        return
    visited[current] = True
    for g in graph[current]:
        if len(graph[current]) == 2 and current != answer[0]:
            answer[3] += 1
            return
        dfs(graph,visited,g,answer)
            
def solution(edges):
    answer = [0] * 4
    graph = defaultdict(list)
    visited = defaultdict(lambda: False)
    for edge in edges:
        s,d = edge
        graph[s].append(d)
    cadidate = set([ edge[0] for edge in edges]) - set([ edge[1] for edge in edges])
    for c in cadidate:
        if len(graph[c]) >= 2:
            root = c
            answer[0] = root
    dfs(graph,visited,root,answer)
    # 도넛 -> 다시 돌아 오는데 1개의 edge만 있으면 도넛,
    # 막대 -> 가다가 끊기면 막대
    # 8자 -> 다시 돌아오는데 여러개의 edge가 있으면 8자
    
    # 2개이상 edge를 단방향으로 가지는 것 or 3개이상 
    # source에 있는데 dst에 없음
    # 
    return answer