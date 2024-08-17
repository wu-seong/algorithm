import sys
sys.setrecursionlimit(10**6)
answer = []
def dfs(graph, current, sources):
    # 티켓을 완전히 소진하는 것이 목적
    if not graph[current]:
        all_visited = True
        for g in graph:
            if graph[g]:
                all_visited = False
                return
        if all_visited:
            global answer
            t = current
            answer.append(t)
            while not (t == "ICN" and not sources['ICN']):
                t = sources[t].pop()
                answer.append(t)
            answer = answer[::-1]
        return
    for dst in reversed(graph[current]):
        graph[current].remove(dst)
        sources[dst].append(current)
        dfs(graph, dst, sources)
        if answer:
            return
        graph[current].append(dst)
        sources[dst].pop()
    # 티켓은 사용 시에 제거
    # 호출로 돌아오면 티켓 복구
    

    # 방문 시 이전 목적지를 차례로 저장
    return
def solution(tickets):
    # 그래프 정보 만들기
    graph = {}
    sources = {}
    for t in tickets:
        s,d = t
        if s not in graph:
            graph[s] = []
        if s not in sources:
            sources[s] = []
        if d not in sources:
            sources[d] = []
        if d not in graph:
            graph[d] = []
        
        graph[s].append(d)
    for g in graph:
        graph[g].sort(reverse=True)
    # dfs로 완전 탐색 
    for f_dst in reversed(graph["ICN"]):
        graph["ICN"].remove(f_dst)
        sources[f_dst].append("ICN")
        dfs(graph, f_dst, sources)
        if answer:
            break
        graph["ICN"].append(f_dst)
        sources[f_dst].pop()
    # 저장한 이전 목적지로 역추적
    #print(answer)
    return answer
