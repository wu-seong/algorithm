from collections import deque

N,K = map(int, input().split())
visited = [False for _ in range(1000000)]

queue = deque()
root = (N,0)
visited[root[0]] = True
queue.append(root)
while queue:
    position, sec = queue.popleft()
    if position == K:
        print(sec)
        exit()
    if not visited[position+1]:
        visited[position+1] = True
        queue.append((position+1, sec+1))
    if position*2 <= 100000 and not visited[position*2]:    
        visited[position*2] = True
        queue.append((position*2, sec+1))
    if position-1 >= 0 and not visited[position-1]:    
        visited[position-1] = True
        queue.append((position-1, sec+1))

    