def solution(p):
    '''
    균형잡힌 괄호 문자열을 올바른 괄호 문자열로 바꾸는 작업
    
    괄호 문자열을 ->균형잡힌 괄호 문자열과 나머지로 분리
    
    2가 올바르면 앞에 붙이기
    올바르지 않으면 ex) ')(', '))((', ')))((('...
    v에 대해 재귀적으로 수행된 문자열을 감싸기
    
    더 이상 분리될 수 없는 균형 잡힌 괄호 문자열을 찾아야함
    여는 괄호 + 1 닫는 괄호 -1해서 0이 될 때 까지 찾기
    '''
    def recur(p): # 문자열 나누고 판단해서 올바른 문자열로 반환
        if not p: # 빈 문자열 판단
            return ""
        balance = 0
        for i, ch in enumerate(p): # 문자열 나누기
            if ch == '(':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                b_str = p[:i+1]
                rest = p[i+1:]
                break
        #print(b_str, rest)

        def is_right(s): # 문자열 판단 함수
            stack = []
            for ch in s:
                if ch == '(':
                    stack.append('(')
                else:
                    if not stack or stack.pop() != '(':
                        return False
            if stack:
                return False
            return True

        if is_right(b_str):  #문자열 판단해서 올바르게 만들기 및 재귀호출
            return b_str + recur(rest)
        else:
            result = "(" + recur(rest) + ")"
            b_str = list(b_str[1:-1])
            for i in range(len(b_str)):
                if b_str[i] == '(':
                    b_str[i] = ')'
                else:
                    b_str[i] = '('
            result += "".join(b_str)
            return result
    return recur(p)
    '''
    얻은 문자열 빈 문자열 판단하기,
    분리하기
    u를 판단하고 올바르면 v에 대해 재귀 호출 + u에 이어 붙이기
    아니면 v에 대해 재귀 호출 + 올바르게 만들기
    
    '''
    
    