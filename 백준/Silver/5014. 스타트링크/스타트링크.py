from collections import deque
F, S, G, U, D = map(int, input().split())

queue = deque()
visited = [False for _ in range(F+1)]
root = (S,0)
queue.append(root)
while queue:
    s, l = queue.popleft()
    if s == G:
        print(l)
        exit()
    if s+U <= F and not visited[s+U]:
        visited[s+U] = True
        queue.append((s+U, l+1))
    if s-D >= 1 and not visited[s-D]:
        visited[s-D] = True
        queue.append((s-D, l+1))
print("use the stairs")