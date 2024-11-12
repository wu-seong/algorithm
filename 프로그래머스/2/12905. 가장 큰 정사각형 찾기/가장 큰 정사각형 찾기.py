def solution(board): 
    '''
    1,1부터 -1,-1 대각선 -1이 모두 1이면 -> 2
    1, 2
    1, 3
    1, N-1
    ...
    N-1,1
    N-1,2
    ...
    N-1,N-1
    '''
    
    '''
    현재 위치가 1이면 나머지 3군데 위치 중 가장 작은 것 + 1
    '''
    n,m = len(board), len(board[0])
    
    for i in range(1,n):
        for j in range(1,m):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                
    result = 0
    for b in board:
        result = max(result, max(b))
    return result ** 2