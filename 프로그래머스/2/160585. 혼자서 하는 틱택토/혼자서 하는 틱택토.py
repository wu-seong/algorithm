from copy import deepcopy
def solution(target):
    '''
    틱택토를 하면서 나올 수 있는 모든 경우의 수를 board에 저장
    3개가 연속되는 것이 있으면 더 이상 진행할 필요 없음
    
    처음에 O 선공해서 9개 중 하나 놓고 나머지 게임 진행하면서 보드 저장
    만약 3개가 모이면 중단
    XO가 바뀌는 걸로도 저장
    
    저장하는 연산이 약 300만
    
    '''
    boards = set()
    board = [['.' for _ in range(3)] for _ in range(3)]
    boards.add('.........')
    print(board)
    
    def is_fin(me):
         # 마지막으로 둔게 O이면 O만 체크
        for line in board: # 가로 줄 확인
            if "".join(line) == me*3:
                return True
        # 세로 줄 확인
        for i in range(3):
            for line in board:
                if line[i] != me:
                    break
            else: # 세로줄이 모두 다 O/X 이면
                return True
        # 대각선 확인
        if (board[0][0] == me and board[1][1] == me and board[2][2] == me) or (board[1][1] == me and board[0][2] == me and board[2][0] == me):
            return True
        return False
    
    #print(board, is_fin('O'))
    check = "OX"
    def ttt(level, i, j):
        nonlocal board, boards
        #print(level, board)
        if level == 9:
            return
        # 현재 위치에 표시하기
        board[i][j] = check[level%2]
        # 게임 종료 판단하기
        if is_fin(check[level%2]):
            boards.add("".join(board[0]) + "".join(board[1]) + "".join(board[2]))
            board[i][j] = '.'
            return
        # 안 끝나면 boards에 저장
        boards.add("".join(board[0]) + "".join(board[1]) + "".join(board[2]))
        # 다음 놓을 위치 재귀
        for n_i in range(3):
            for n_j in range(3):
                if board[n_i][n_j] == '.':
                    ttt(level + 1, n_i, n_j)
        # 현재 위치 회수
        board[i][j] = '.'
    for i in range(3):
        for j in range(3):
            ttt(0,i,j)
    #print('target: ', target[0] + target[1] + target[2])
    # for b in boards:
    #     print(b)
    if target[0] + target[1] + target[2] in boards:
        return 1
    return 0