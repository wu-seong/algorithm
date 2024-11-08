from collections import defaultdict
from heapq import *
def solution(N, roads, K):
    '''
    다익으로 풀어서 비용을 비교하면 되는데
    다익이 기억이 안나네..
    
    각 노드 마다 최단거리 무한으로 초기화 해놓고
    
    현재까지 방문한 노드 중에서 갈 수 있는 노드 중 가장 짧은 가중치를 먼저 가는거였나
    그래서 아마 힙에 가중치를 비교해서 노드를 넣었던 듯?
    
    꺼내서 최신화가 필요한 노드가 맞는지 확인 한번하고
    
    현재 노드에서 갱신할 수 있는 것을 갱신하고 heap에 푸시
    '''
    graph = defaultdict(list)
    for a,b,w in roads:
        graph[a].append((b,w))
        graph[b].append((a,w))
    #print(graph)
    distance = [float('inf')] * (N+1)
    
    
    def dijkstra(start):
        q = []
        distance[start] = 0
        heappush(q,(start, 0))
        
        while q:
            current, cost = heappop(q)
            
            if cost > distance[current]:
                continue
            for v,w in graph[current]:
                new_cost = w + cost
                if new_cost < distance[v]:
                    distance[v] = new_cost
                    heappush(q, (v,new_cost))
                    
    dijkstra(1)                
    #print(distance)
    cnt = 0
    for dist in distance:
        if dist <= K:
            cnt += 1
    return cnt
            
        