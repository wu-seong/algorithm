import copy
def search_last(board):
    for i in range(10,-1,-1):
        if board[i] != 0:
            return i
def calculate(board):
    score = 0
    for i in range(11):
        if board[i] > 0:
            if board[i] > 1:
                score += (10-i)
            score += (10-i)
    return score
def dfs(board, current, remain_arrow):
    global max_score
    global max_board
    #print(current, board)
    if current == 10: # 스코어 최댓값 비교
        # 남은 화살은 0점에 모두 쏘기
        board[current] += remain_arrow
        score = calculate(board)
        if max_score <= score:
            if max_score == score:
                max_last = search_last(max_board)
                last = search_last(board)
                if last <= max_last:
                    board[current] = 0
                    return
            max_score = score
            max_board = copy.deepcopy(board)
        board[current] = 0
        return
    # 남아 있는 화살이 0일 때
    if remain_arrow == 0:
        score = calculate(board)
        if max_score <= score:
            if max_score == score:
                max_last = search_last(max_board)
                last = search_last(board)
                if last <= max_last:
                    board[current] = 0
                    return
            max_score = score
            #print(score)
            max_board = copy.deepcopy(board)
            #print(max_board)
        return
    # 각 점수 마다 분기 나누기
    need_arrow = apche_board[current] + 1
    if need_arrow <= remain_arrow:
        board[current] = need_arrow 
        dfs(board, current+1, remain_arrow - need_arrow) # 쏘는 분기
        board[current] = 0
    dfs(board, current+1, remain_arrow) # 안 쏘는 분기
    
max_score = 0
max_board = []
apche_board = []

def solution(n, info):
    global apche_board
    apche_board = info
    apche_score = 0
    for i in range(11):
        if apche_board[i] > 0:
            apche_score += 10-i
    board = [0] * 11
    dfs(board, 0, n)
    if max_score <= apche_score:
        return [-1]
    return max_board
    #print(max_board)

