def solution(ingredient):
    # 재료가 스택으로 쌓임 1 2 3 1 
    # 앞에 재료부터 스택에 넣는다
    # 넣을 때 마다 마지막이 1231인지 확인
    # 맞으면 스택 슬라이싱
    stack = []
    cnt = 0
    for ig in ingredient:
        stack.append(ig)
        if len(stack) >= 4:
            if stack[-4:] == [1,2,3,1]:
                cnt += 1
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
    return cnt
                
    
    