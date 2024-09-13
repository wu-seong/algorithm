import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
    q = []

    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
            #print(now, dist)

        if dist > distance[now]:
            continue

        for v,w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost,v))
    
# 그래프 정보 저장 (출발지 - 도착지 위치 같을 시에는 경로값 작은 것으로)
# 도착 위치가 D보다 크면 저장하지 않음
N,D = map(int, input().rstrip().split())

graph = [[] for _ in range(D+1)]
for _ in range(N):
    u,v,w = map(int, input().rstrip().split())
    if v > D:
        continue
    graph[u].append((v,w))
for i in range(D):
    graph[i].append((i+1,1))
    #print(graph)
distance = [ float('inf') for _ in range(D+1)]

dijkstra(0)
    #print(distance)
print(distance[D]) # 그 중 가장 작은 것 선택

