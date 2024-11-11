from copy import deepcopy
def solution(expression):
    '''
    연산자 조합 다해보기
    6개
    * + -
    '''
    n = len(expression)
    op_list = '*+-'
    def calculator(op1, op2, operate):
        #print(op1,op2,operate)
        if operate == '*':
            return int(op1) * int(op2)
        elif operate == '+':
            return int(op1) + int(op2)
        elif operate == '-':
            return int(op1) - int(op2)
    
    '''
    연산자 우선 순위대로 먼저 계산하면서 값 갱신하기
    표현을 리스트로 바꾸기
    우선순위에 있는 연산자 찾으면 앞 뒤 연산해서 바꾸기
    '''
    expression = expression.replace('*',',*,')
    expression = expression.replace('+',',+,')
    expression = expression.replace('-',',-,')
    expression = list(expression.split(','))
    origin = deepcopy(expression)
    #print(expression)
    order_list = ['*+-', '*-+', '+-*', '+*-', '-+*', '-*+']
    max_result = 0
    for order in order_list:
        for operator in order:
            i = 1
            while i < len(expression):
                if expression[i] == operator:
                    temp = calculator(expression[i-1], expression[i+1], expression[i])
                    del expression[i+1]
                    expression[i] = temp
                    del expression[i-1]
                    continue
                i += 1
        max_result = max(max_result, abs(expression[0]))
        #print(expression)
        expression = deepcopy(origin)                
    return max_result
            
            