from collections import deque
'''
올바른 괄호 끼리는 덧셈, 괄호 덧붙이기 가능

push/pop, 

pushleft/popleft

deque 만들기 

0 ~ n-1 까지
popleft -> append

올바른 괄호인지 판단하기

'''
# 문자열이 올바른 괄호인지 판단하는 함수
def is_right(s):
    #print(s)
    stack = []
    pair = {'(': ')' , '{': '}', '[': ']'}
    for v in s:
        # 여는 괄호 집합이면 stack에 저장
        if v in ['(', '{','[']:
            stack.append(v)
        # 닫는 괄호 집합이면 stack이 비지 않은지, 마지막 것과 짝궁인지 판단
        else:
            if not stack:
                return False
            last = stack.pop()
            #print('v = last', v, pair[last])
            if v != pair[last]:
                return False
    if stack:
        return False
    return True
        
def solution(s):
    cnt = 0
    deq = deque(s)
    for _ in range(len(deq)):
        if is_right(deq):
            #print('count')
            cnt += 1
        deq.append(deq.popleft())
    return cnt
    