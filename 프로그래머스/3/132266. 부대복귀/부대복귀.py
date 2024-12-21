'''
주어진 그래프에서
각 지역에서 주어진 destination까지 가는 것 생각하기
destination을 시작점으로 다익스트라 돌리기
그다음 sources에 있는 순서대로 result에 담기
'''
from collections import defaultdict
from heapq import heappush, heappop
def solution(n, roads, sources, destination):
    result = []
    dist = [float('inf') for _ in range(n+1)]
    
    graph = defaultdict(list)
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)
    
    def dijkstra(start):
        q = []
        dist[start] = 0
        heappush(q, (start,0))
        
        while q:
            n, w = heappop(q)
            
            if dist[n] < w:
                continue
            
            for next in graph[n]:
                if w + 1 < dist[next]:
                    heappush(q, (next, w + 1 ))
                    dist[next] = w + 1
    dijkstra(destination)
    #print(dist)
    for i in sources:
        if dist[i] == float('inf'):
            result.append(-1)
            continue
        result.append(dist[i])
    #print(result)        
    return result
            
        