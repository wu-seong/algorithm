import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write
def dijkstra(start):
    q = []

    # 첫 시작점 방문 및 거리 초기화
    heapq.heappush(q,(0,start))
    distance[start] = 0

    # 방문할 곳이 없을 때 까지 가장 최단거리 방문하기
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]: # 현재 방문한 경로값이 더 크면 이전에 방문했던 것
            continue

        for v,w in graph[now]: # 이 다음 방문할 노드를 넣기
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

V,E = map(int, input().rstrip().split())
start = int(input().rstrip())

# 거리 정보 저장할 배열
distance = [float('INF')] * (V+1)
    #print(distance)
# 그래프 정보 저장
graph = [ [] for _ in range(V+1)]
    #print(graph)
for i in range(E):
    u,v,w = map(int, input().rstrip().split())
    graph[u].append((v,w))
    #print(graph)

dijkstra(start)

for i in range(1,V+1):
    if distance[i] == float('inf'):
        print("%s\n" %'INF')
    else:
        print("%d\n" %distance[i])

