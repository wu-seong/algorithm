import sys
input = sys.stdin.readline

from collections import deque


N = int(input().rstrip())

q = deque()            
def queue(c):
    if c[:4] == 'push':
        value = int(c.split(' ')[1])
        q.append(value)
    elif c == 'pop':
        if not q:
            print(-1)
            return
        print(q.popleft())
    elif c == 'size':
        print(len(q))
    elif c == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif c == 'front':
        if not q:
            print(-1)
            return
        print(q[0])
    elif c == 'back':
        if not q:
            print(-1)
            return
        print(q[-1])
for _ in range(N):
    queue(input().rstrip())