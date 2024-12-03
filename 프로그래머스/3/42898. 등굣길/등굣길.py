def solution(m, n, puddles):
    '''
    왼쪽과 위에서 경로를 더한 것이 현재의 경로
    0,0은 1임
    1열부터 쭉 가다가 물이 만나면 break
    
    1행부터는
    0열은 위에서 가져오고 
    1열부터는 왼쪽 위 더한 것, 중간에 물을 만나면 continue
    '''
    # m*n 배열 만들고 물 표시
    puddles = [ (x-1,y-1) for x,y in puddles]
    puddles = set(puddles)
    print(puddles)
    board = [[0 for _ in range(m)] for _ in range(n)]
    
    board[0][0] = 1
    for j in range(1,m):
        if (j,0) in puddles:
            break
        board[0][j] = 1
    
    for i in range(1,n):
        for j in range(m):
            if (j,i) in puddles: # 물일 떄
                continue
            if j == 0:
                board[i][j] = board[i-1][j]
            else:
                board[i][j] = (board[i-1][j] + board[i][j-1]) % 1000000007
    # for b in board:
        #print(b)
    return board[n-1][m-1]
    
    