def solution(s):
    open = 0
    # 여는 괄호가 나오면 카운팅, 닫는 괄호가 나오면 역 카운팅
    # 만약 카운팅이 0이하인데 닫는 괄호가 나오면 잘못된 괄호이다.
    for c in s:
        if c == '(':
            open += 1
        else:
            if open <= 0:
                return False
            open -= 1
    # 만약 문자열이 끝났는데 괄호가 안 닫혀있으면 잘못된 괄호이다.
    if open > 0:
        return False
    return True