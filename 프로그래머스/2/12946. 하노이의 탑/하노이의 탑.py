def solution(n):
    '''
    원판을 일단 가장 아래있는 것 부터 옮겨야 하는데
    그러려면 나머지 것들이 2번에 모두 있어야 함
    그러려면 3번에 나머지 것들이 있어야 함
    
    
    start 에서 dest 까지 n개를 옮기려면
    현재 start에 있는 가장 바닥을 dest에 옮겨야 함
    
    n == 1일 때는 1
    n > 1일 때는
    start 에서 mid 까지 n-1개를 옮기기
    
    그다음에 start에 있는 것을 dest에 옮기고
    다시 mid에 있는 바닥것을 dest에 옮기기 
    
    '''
    result = []
    def hanoi(start, mid, dest, n):
        nonlocal result
        if n == 1:
            #print(start, dest, "로 이동")
            result.append([start, dest])
            return
        hanoi(start, dest, mid, n-1)
        result.append([start, dest])
        #print(start, dest, "로 이동")
        hanoi(mid, start, dest, n-1)
    hanoi(1,2,3,n)
    print(result)
    return result
        
        
            