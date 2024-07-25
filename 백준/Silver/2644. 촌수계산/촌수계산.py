from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

# N < 100
n = int(input().rstrip())
p1, p2 = map(int, input().rstrip().split())
m = int(input().rstrip())

graph = [[] for _ in range(n+1)]
for i in range(m):
    x,y = map(int, input().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

#print("%s\n" %graph)

queue = deque()
visited = [False] * (n+1)
root = p1

queue.append([root, 1])
visited[root] = True

while queue:
    value, currentDepth = queue.popleft()
    for node in graph[value]:
        if node == p2:
            print("%d\n" %currentDepth)
            exit()
        if not visited[node]:
            visited[node] = True
            queue.append([node, currentDepth+1])
print("%d\n" %-1)

    