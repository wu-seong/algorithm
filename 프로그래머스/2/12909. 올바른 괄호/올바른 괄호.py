'''
(와 )는 짝궁이어야함
-> 닫는 괄호가 왔을 때, 여는 괄호가 없으면 오류, 다 지났는데 괄호가 안닫혀도 오류

( 가 오면 스택에 push )가 오면 스택에서 pop
)가 왔는데 스택이 empty이면 오류
다 순회했는데 스택이 empty가 아니면 오류
'''
def solution(s):
    stack = []
    #print(stack)
    for v in s:
        if v == ')':
            if stack:
                stack.pop()
            else:
                return False
        else:
            stack.append(0)
    if stack:
        return False
    return True
                
            
            