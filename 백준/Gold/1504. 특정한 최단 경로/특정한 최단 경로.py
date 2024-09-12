import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
    q = []

    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 방문한건 패스
        if dist > distance[now]:
            continue
        
        for v,w in graph[now]:
            cost = w + dist
            if cost < distance[v]: # 더 최소 경로이거나 특정 정점이면 방문
                distance[v] = cost
                heapq.heappush(q, (cost,v))

N,E = map(int, input().rstrip().split())

graph = [ [] for _ in range(N+1)]
for i in range(E):
    u,v,w = map(int, input().rstrip().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
    #print(graph)
A,B = map(int, input().rstrip().split())

distance = [float('inf')] * (N+1)
r1,r2 = 0,0
dijkstra(1)
r1 += distance[A]
r2 += distance[B]
distance = [float('inf')] * (N+1)
dijkstra(A)
r1 += distance[B]
distance = [float('inf')] * (N+1)
dijkstra(B)
r1 += distance[N]
r2 += distance[A]
distance = [float('inf')] * (N+1)
dijkstra(A)
r2 += distance[N]
answer = min(r1,r2)
if answer == float('inf'):
    print(-1)
    exit()
print(answer)

