def append_result(result, stack, value,i):
    while stack and stack[-1][0] > value: #더 큰 값은 모두pop empty까지
        v, index = stack.pop()
        # result의 index에 빼온 주식의 index, 값은 i - index
        result[index] = i-index

def last_append_result(result, stack, i):
    while stack: #더 큰 값은 모두pop empty까지
        v, index = stack.pop()
        # result의 index에 빼온 주식의 index, 값은 i - index
        #print(index, i-index)
        result[index] = i-index
    
def solution(prices):
    # 이후에 몇번째에 더 작은 값이 나오는지 
    # 하나씩 pop하면서 새로운 배열에 push 및 연속 오름 카운팅
    # 만약 마지막 push된 값보다 더 작은 값이 나오면 -> 해당 값보다 큰 값은 모두 pop 및 카운팅 저장
    # 마지막 원소이면 현재까지 있는 배열을 모두 pop하면서 카운팅 저장
    stack = []
    n = len(prices)
    result = [0]*n
    for i in range(n):
        if not stack or prices[i] >= stack[-1][0]: # 비었거나 더 크거나같은 값이 오면 push
            stack.append((prices[i],i))
        else: # 더 작은 값이 올 경우
            append_result(result, stack, prices[i],i)
            stack.append((prices[i],i))
    if stack: # 남은 stack 다 털기
        last_append_result(result,stack,n-1)
    #print(result)
    return result
        