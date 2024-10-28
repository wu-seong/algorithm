def get_down_point(board,m,i,j):
    # 빈칸이 아닌 지점을 찾거나 바닥까지 내려왔을 때 까지 반복
    while i < m:
        if board[i][j] != '-':
            return i-1
        i += 1
    return i-1
        
def move_block(board,m,n):
    # 아래서 부터 위로
    # 내 아래가 빈칸이면 내려보내기
    for i in range(m-2,-1,-1): # m = 4 -> 2 1 0
        for j in range(n):
            value = board[i][j]
            if value == '-': # 본인이 빈칸이면 내려보내지 않음
                continue
            if board[i+1][j] == '-': # 나의 아래가 빈칸임
                #print("내 아래가 빈칸임",i,j)
                down_point = get_down_point(board,m,i+1,j)
                board[down_point][j] = value
                board[i][j] = '-'
    
    
def add_remove_set(y,x, board, remove_set,m,n): # 현재 블록을 기준으로 근처에 없애야할 블록 위치를 추가
    target = board[y][x]
    #print("타겟",target)
    if target == '-':
        return
    # 좌상 우상 좌하 우하
    check_list = [[(-1,-1),(-1,0),(0,-1)],[(-1,0),(-1,1),(0,1)],[(0,-1),(1,-1),(1,0)],[(0,1),(1,1),(1,0)]]
    for check in check_list: #4개 묶음을 순회
        add_list = []
        same = True
        for dy,dx in check: # 각 묶음의 블록을 순회
            yy = y+dy
            xx = x+dx
            if 0 <= yy < m and 0<= xx < n: # 존재하는 블록만 순회
                if board[yy][xx] == target: # 같으면 삭제 리스트에 추가
                    add_list.append((yy,xx))
                else: # 다르면 끝
                    same = False
                    break
            else: #존재하지 않는 블록이 있으면 끝
                same = False
                break
        if same: # 모든 블록이 존재하고 같으면 삭제 리스트 업데이트
            remove_set.update(set(add_list))
                    
def solution(m, n, board):
    board = [ [ board[i][j] for j in range(n)] for i in range(m) ]
    total_cnt = 0 # 결과 카운팅
    c = 4
    while True:
        remove_set = set() # 삭제할 리스트 
        for y in range(m): # 각 블록 하나하나 체크하면서 -로 만들 블록들 set에 저장
            for x in range(n):
                if board[y][x] == '-':
                    continue
                add_remove_set(y,x, board, remove_set,m,n)
        #print(remove_set)
        for y,x in remove_set: # 다 찾은 뒤에 -로 만들면서 카운팅하기
            board[y][x] = '-'
            
        cnt = len(remove_set) 
        if cnt == 0: # 더 이상 터질 것이 없으면 끝
            return total_cnt
        total_cnt += cnt
        # 그위에 있는 것들 아래로 채우기
        move_block(board,m,n)
    

    
    