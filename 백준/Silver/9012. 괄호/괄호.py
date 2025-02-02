import sys
input = sys.stdin.readline

N = int(input().rstrip())

for _ in range(N):
    stack = []
    s = input().rstrip()
    for ch in s:
        if ch == ')':
            if not stack:
                stack.append(0)
                break
            else:
                stack.pop()
        else:
            stack.append(0)
    #print(stack)
    if stack:
        print('NO')
    else:
        print('YES')
      