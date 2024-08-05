import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())

graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)

# 그래프 연결하기
for i in range(N-1):
    start, end = map(int, input().rstrip().split())
    graph[start].append(end)
    graph[end].append(start)

# 1번부터 탐색하면서 부모 노드 저장하기
queue = deque()
visited[1] = 0
queue.append(1)

while queue:
    node = queue.popleft()
    for next in graph[node]:
        # 방문하지 않았다면 방문
        if visited[next] == -1:
            #현재 노드 번호를 저장
            visited[next] = node
            queue.append(next)
for i in range(2,N+1):
    print(visited[i])