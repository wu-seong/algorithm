import sys
import heapq
input = sys.stdin.readline

def dijkstra(start, g):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for v,w in g[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

V,E,X = map(int, input().rstrip().split())

graph = [ [] for _ in range(V+1)]
r_graph = [ [] for _ in range(V+1)]
for i in range(E):
    u,v,w = map(int, input().rstrip().split())
    graph[u].append((v,w))
    r_graph[v].append((u,w))
    #print(graph)
    
distance = [float('inf')] * (V+1)
total_cost = [0]*(V+1)
dijkstra(X, graph)
for i in range(1,V+1):
    total_cost[i] += distance[i]
    #print(distance)
distance = [float('inf')] * (V+1)
dijkstra(X, r_graph)
for i in range(1,V+1):
    total_cost[i] += distance[i]
    #print(distance)
    #print(total_cost) 
print(max(total_cost))

# 그래프를 역방향으로 바꾸면
# 모든 지점 -> X로 가는 최소비용을 다익스트라 1번으로 구할 수 있다. (X를 시작지점으로 역방향 다익스트라)
# 다익스트라의 대칭적인 특성(역방향으로 바뀌어도 경로만 반대로 바뀌고 출발지 - 목적지 비용은 같다.)