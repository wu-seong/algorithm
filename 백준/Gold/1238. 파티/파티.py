import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for v,w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))


V,E,X = map(int, input().rstrip().split())

graph = [ [] for _ in range(V+1)]
for i in range(E):
    u,v,w = map(int, input().rstrip().split())
    graph[u].append((v,w))
    #print(graph)
    
distance = [float('inf')] * (V+1)
# A에서 다익스트라
total_cost = [0]*(V+1)
dijkstra(X)
for i in range(1,V+1):
    total_cost[i] += distance[i]
    #print(distance)
for i in range(1,V+1):
    distance = [float('inf')] * (V+1)
    dijkstra(i)
    total_cost[i] += distance[X]
    #print(distance) 
print(max(total_cost))
# Z보다 큰 것들은 
# A 에서 