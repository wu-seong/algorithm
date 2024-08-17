from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
answer = []
def dfs(graph, current, footprint):
    global answer
    # 티켓을 완전히 소진하는 것이 목적
    if not graph[current]:
        all_visited = True
        for g in graph:
            if graph[g]:
                all_visited = False
                return
        if all_visited:
            footprint.append(current)
            answer = footprint
        return
    for dst in reversed(graph[current]):
        graph[current].remove(dst)
        footprint.append(current)
        dfs(graph, dst, footprint)
        if answer:
            return
        graph[current].append(dst)
        footprint.pop()
    return
def solution(tickets):
    # 그래프 정보 만들기
    graph = defaultdict(list)
    footprint = []
    for t in tickets:
        s,d = t
        graph[s].append(d)
    for g in graph:
        graph[g].sort(reverse=True)
    # dfs로 완전 탐색 
    for f_dst in reversed(graph["ICN"]):
        graph["ICN"].remove(f_dst)
        footprint.append("ICN")
        dfs(graph, f_dst, footprint)
        if answer:
            break
        graph["ICN"].append(f_dst)
        footprint.pop()
    #print(answer)
    return answer
