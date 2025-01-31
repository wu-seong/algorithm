import sys
input = sys.stdin.readline
stack = []
def command(s):
    if s[:4] == ('push'):
        stack.append(int(s.split(' ')[1]))
    elif s == 'pop':
        if not stack:
            print(-1)
            return
        print(stack.pop())
    elif s == 'size':
        print(len(stack))
    elif s == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif s == 'top':
        if not stack:
            print(-1)
            return
        print(stack[-1])
    
N = int(input())
for _ in range(N):
    command(input().rstrip())