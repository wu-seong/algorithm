def solution(n):
    '''
    144C12 -> 개큼 완탐 x
    
    백트래킹
    
    첫번째행에 0~n-1까지 두고
    
    그다음 것 이전 것들과 겹치는지 확인
    겹치지 않으면 두고 겹치면 그 다음 것으로
    겹침 유무확인
    가로 확인
    대각선 확인
    i가 n까지 오면 1개 성공
    '''
    cnt = 0
    
    board = [[0 for _ in range(n)] for _ in range(n)]
    print(board)
    def queen(col, row):
        nonlocal cnt, board
        #print(col, row, board)
        # level == n 이면 종료하고 카운팅
        # 현재 두는 것 배치 확인
        for i in range(col):
            if board[row][i]:
                return
        i = col - 1
        j = row - 1
        while i >= 0 and j >= 0: # 왼쪽 위
            if board[j][i]:
                return
            i -= 1
            j -= 1
        i = col - 1
        j = row + 1
        while i >= 0 and j < n: # 왼쪽 아래
            if board[j][i]:
                return     
            i -= 1
            j += 1
        # 가능하면 퀸 놓기
        # 1에서 N까지 재귀
        board[row][col] = 1
        for i in range(n):
            if col + 1 == n: # 성공 시 카운팅
                cnt += 1
                break
            queen(col + 1, i)
        board[row][col] = 0
    for i in range(n):
        queen(0,i)
    print(cnt)
    return cnt