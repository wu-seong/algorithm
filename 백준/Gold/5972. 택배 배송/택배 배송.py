import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
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


V,E = map(int, input().rstrip().split())

graph = [ [] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int, input().rstrip().split())
    graph[u].append(((v,w)))
    graph[v].append(((u,w)))
    #print(graph)
distance = [float('inf')] * (V+1)
dijkstra(1)
print(distance[V])