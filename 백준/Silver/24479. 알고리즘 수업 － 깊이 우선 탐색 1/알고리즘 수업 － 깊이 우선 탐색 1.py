import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, node, visited_order):
    global order
    visited_order[node] = order
    order += 1
    for adj_n in graph[node]:
        if visited_order[adj_n] == 0:
            dfs(graph,adj_n,visited_order)

N, M, R = map(int, input().rstrip().split())

graph = [ [] for _ in range(N+1)]
visited_order = [ 0 for _ in range(N+1)]

# 그래프 정보 저장
for _ in range(M):
    start, end = map(int, input().rstrip().split())
    graph[start].append(end)
    graph[end].append(start)

# 오름차순 정렬
for adj_ns in graph:
    adj_ns.sort()
order =  1
dfs(graph, R, visited_order)
# 순서 출력
for i in range(1, N+1):
    print(visited_order[i])