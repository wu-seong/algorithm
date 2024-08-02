import sys
from collections import deque


input = sys.stdin.readline
print = sys.stdout.write
N,M = map(int, input().rstrip().split())

visited = set() 
queue = deque()

visited.add(N)
previous = {}
previous[N] = -1
queue.append((N,0))

origin = deque()
while queue:
    x,t = queue.popleft()
    if x == M:
        print("%d\n" %t)
        spot = M
        while True:
            origin.append(spot)
            spot = previous[spot]
            if spot == -1:
                while origin:
                    print("%d " %origin.pop())
                print("\n")
                exit()
    for dx,a in [(1,1),(-1,1),(0,2)]:
        xx = a*x+dx
        if 0 <= xx <= 100000:
            if not xx in visited:
                previous[xx] = x
                visited.add(xx)
                queue.append((xx,t+1))

    


