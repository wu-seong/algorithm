
def solution(order):
    # 바로 일치할 때와 보조에서 일치할 때 카운팅
    # stack에 넣는것까지 시뮬 돌려도 괜찮을듯?
    queue = [i for i in range(len(order),0,-1)]
    #print(queue)
    stack = []
    # 빼면서 순서에 맞으면 카운팅
    # 안맞으면 stack한번 확인해보기 stack에도 없으면 stack에 넣기
    i = 0
    while queue: # queue가 빌 때 까지 빼기
        # 만약 order랑 같다면 order += 1
        num = queue.pop()
        #print(stack, num, order[i])
        if num == order[i]:
            i += 1
        else: # 없으면 stack에 넣기
            stack.append(num)
            
        while stack and order[i] == stack[-1]: # 스택이 존재하고 마지막 물건이 같을 때 까지 빼기
            stack.pop()
            i += 1
            # 
    #print(i)
    return i
                    
                
                
    #5 4 3 2 1  
    # 1 2 3 4 5