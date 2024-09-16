import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if now != (V-1) and visiable[now] == 1: # 시야에 보이면 못감
            continue
        if dist > distance[now]:
            continue
        for v,w in graph[now]:
            if v != (V-1) and visiable[v] == 1:
                continue
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost,v))


V,E = map(int ,input().rstrip().split())
visiable = list(map(int, input().rstrip().split()))
graph = [ [] for _ in range(V)]
for _ in range(E):
    u,v,w = map(int, input().rstrip().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
    #print(visiable, graph)
distance = [float('inf')] * (V)

dijkstra(0)
    #print(distance)
if distance[V-1] == float('inf'):
    print(-1)
    exit()
print(distance[V-1])
