from collections import deque
def is_right(s):
    end = [']','}',')']
    start= ['[','{','(']
    stack = []
    # 읽어온 문자가 닫는 괄호이면
    # stack에서 pop을 할 때 해당 문자의 여는 괄호가 와야 함
    # 여는 괄호면 stack에 넣기
    # 그렇지 않으면 false
    for c in s:
        for i in range(3):
            if start[i] == c:
                stack.append(end[i]) # 다음에 와야할 괄호를 저장
            elif end[i] == c:
                if not stack or stack.pop() != c:
                    return False
    # 마지막에 괄호가 닫히지 않았어도 false
    if stack:
        return False
    return True
def solution(s):
    # 완전탐색
    # 문자열을 0~s길이-1 만큼 회전 시키며 올바른 괄호인지 확인
    # 회전 = 첫번째에서 popleft하여 push하는것
    cnt = 0
    s = deque(s)
    for i in range(len(s)):
        if is_right(s):
            cnt += 1
        s.append(s.popleft())
    return cnt