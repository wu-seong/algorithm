import sys
from collections import deque
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    k = int(input().rstrip())
    r_y, r_x = map(int,input().rstrip().split())
    d_y, d_x = map(int,input().rstrip().split())

    visited = [ [False for _ in range(k)] for _ in range(k)]
    queue = deque()

    visited[r_y][r_x] = True
    queue.append((r_y,r_x,0))

    while queue:
        y,x,c = queue.popleft()
        if y == d_y and x == d_x:
            print(c)
            break
        for dy, dx in [ (1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2)]:
            yy = y + dy
            xx = x + dx
            if 0 <= yy < k and 0 <= xx < k:
                if not visited[yy][xx]:
                    visited[yy][xx] = True
                    queue.append((yy,xx,c+1))
