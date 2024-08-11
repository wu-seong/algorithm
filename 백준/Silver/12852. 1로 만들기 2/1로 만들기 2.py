import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
N = int(input().rstrip())

visited = {}
n = N

queue = deque()
queue.append((n,0))
while queue:
    n,c = queue.popleft()
    if n == 1:
        print("%d\n" %c)
        p_queue = deque()
        p_queue.append(n)
        while True:
            if n == N:
                break
            p_queue.append(visited[n])
            n = visited[n]
        while p_queue:
            print("%d " %p_queue.pop())
        print("\n")
        exit()

    operations = [(1,-1)]
    if n % 3 == 0: operations.append((3,0))
    if n % 2 == 0: operations.append((2,0))
    for dn, mn in operations:
        next = n//dn + mn
        #방문하지 않았다면
        if not next in visited:
            visited[next] = n
            queue.append((next,c+1))

    