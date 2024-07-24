import sys
from collections import deque


input = sys.stdin.readline
print = sys.stdout.write
# bfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     for each v ∈ V - {R}

queue = deque()
num_n, num_e, start_n = map(int, input().rstrip().split())

node = [[] for _ in range(num_n+1) ]
visited = [0] * (num_n+1)

for i in range(num_e):
    start, end = map(int, input().rstrip().split())
    node[start].append(end)
    node[end].append(start)

for nodes in node:
    nodes.sort()

c = 1
visited[start_n] = c
queue.append(start_n)
while queue:
    value = queue.popleft()
    for d in node[value]:
        if visited[d] == 0:
            c = c + 1
            visited[d] = c
            queue.append(d)
for i in range(1,num_n+1):
    print("%d\n" %visited[i])
