def solution(s):
    stack = []
    # 문자열 순회하면서 stack의 peek가 현재 문자이면 현재 문자 pop, 아니면 push
    for c in s:
        if stack[-1:] == [c]:
            stack.pop()
        else:
            stack.append(c)
    #print(0 if stack else 1)
    return 0 if stack else 1