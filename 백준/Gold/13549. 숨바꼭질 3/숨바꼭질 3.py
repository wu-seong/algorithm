import sys
from collections import deque
input = sys.stdin.readline

start_x, end_x = map(int, input().rstrip().split())

visited = set()

queue = deque()
visited.add(start_x)
queue.append((start_x,0))
while queue:
    x,t = queue.popleft()
    #print(x,t)
    if x == end_x:
        print(t)
        exit()
    for dx in [-1,1]:
        # 1초에 순간이동 안하는 경우
        if 0 <= x + dx <= 100000:
            if not x + dx in visited:
                visited.add(x+dx)
                queue.append((x + dx,t+1))
        # 순간이동을 하는경우
        if 0 <= 2*x <= 100000:
            if not 2*x in visited:
                visited.add(2*x)
                queue.append((2*x, t))
        


