def get_down_point(board,i,j):
    global m
    # 빈칸이 아닌 지점을 찾거나 바닥까지 내려왔을 때 까지 반복
    while i < m:
        if board[i][j] != '-':
            return i-1
        i += 1
    return i-1
        
def move_block(board):
    global m,n
    # 아래서 부터 위로
    # 내 아래가 빈칸이면 내려보내기
    for i in range(m-2,-1,-1): # m = 4 -> 2 1 0
        for j in range(n):
            value = board[i][j]
            if value == '-': # 본인이 빈칸이면 내려보내지 않음
                continue
            if board[i+1][j] == '-': # 나의 아래가 빈칸임
                down_point = get_down_point(board,i+1,j)
                board[down_point][j] = value
                board[i][j] = '-'
    
    
def add_remove_set(y,x, board, remove_set): # 오른, 아래, 오른아래 확인
    global m,n
    target = board[y][x]
    check= [(0,1),(1,1),(1,0)]
    add_list = []
    same = True
    for dy,dx in check: # 각 묶음의 블록을 순회
        yy = y+dy
        xx = x+dx
        if board[yy][xx] == target: # 같으면 삭제 리스트에 추가
            add_list.append((yy,xx))
        else: # 다르면 끝
            same = False
            break
    if same: # 모든 블록이 존재하고 같으면 삭제 리스트 업데이트
        add_list.append((y,x))
        remove_set.update(set(add_list))
                    
m,n = 0,0
def solution(mm, nn, board):
    global m,n
    m,n = mm, nn
    board = [ [ board[i][j] for j in range(n)] for i in range(m) ]
    total_cnt = 0 # 결과 카운팅
    while True:
        remove_set = set() # 삭제할 리스트 
        for y in range(m-1): # (0,0)~(n-1, m-1)까지 터뜨릴 블록 체크
            for x in range(n-1):
                if board[y][x] == '-': 
                    continue
                add_remove_set(y,x, board, remove_set)
        #print(remove_set)
        
        for y,x in remove_set: # 다 찾은 뒤에 -로 만들고 카운팅
            board[y][x] = '-'
        cnt = len(remove_set) 
        
        if cnt == 0: # 더 이상 터질 것이 없으면 끝
            return total_cnt
        total_cnt += cnt
        # 그위에 있는 것들 아래로 채우기
        move_block(board)

    

    
    