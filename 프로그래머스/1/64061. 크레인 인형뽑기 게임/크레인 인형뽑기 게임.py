from collections import deque
def solution(board, moves):
    # 인형 보드를 옆으로 눕히기
    n = len(board)
    laid_board = [ deque() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                laid_board[j].append(board[i][j])
    
    # for b in board:
    #     print(b)
    # print()
    # for b in laid_board:
    #     print(b)
    
    
            
    # 왼쪽 보드는 2차원 배열로 표현하기
    # 배열에서 뽑는 숫자를 행으로 하여 해당 행의 배열에서 pop하여 인형 타입 얻기
    # 인형이 마지막 것과 같은 타입이라면 pop하기 (stack이 비지 않고) 
    # 그렇지 않으면 push 하기
    stack = []
    cnt = 0
    for m in moves:
        if not laid_board[m-1]:
            continue
        doll_type = laid_board[m-1].popleft()
        if stack and doll_type == stack[-1]:
            cnt += 2
            stack.pop()
            continue
        stack.append(doll_type)
    #print(cnt)
    return cnt
    