import sys
import heapq
input = sys.stdin.readline
def dijkstra(start):
    q = []

    heapq.heappush(q, (0,start))
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

V = int(input().rstrip())
E = int(input().rstrip())
graph =  [ [] for _ in range(V+1)]

for i in range(E):
    u,v,w = map(int, input().rstrip().split())
    graph[u].append((v,w))
    #print(graph)
start, end = map(int, input().rstrip().split())
distance = [float('inf')] * (V+1)
dijkstra(start)
print(distance[end])
