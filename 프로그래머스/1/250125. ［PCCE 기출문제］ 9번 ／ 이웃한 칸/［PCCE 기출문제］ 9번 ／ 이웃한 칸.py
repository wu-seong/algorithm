def solution(board, h, w):
    # h,w에 해당하는 값 가져오기
    # 상하좌우 확인하여 같은 값이면 카운팅
    n = len(board)
    target = board[h][w]
    cnt = 0
    for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        if 0 <= h+dy < n and 0<= w+dx < n:
            if target == board[h+dy][w+dx]:
                cnt += 1
    #print(cnt)
    return cnt