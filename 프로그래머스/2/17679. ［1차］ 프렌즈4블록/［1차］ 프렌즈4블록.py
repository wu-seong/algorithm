'''
810,000
2x2 형태를 확인하기
(x,y+1), (x+1, y), (x+1, y+1)을 확인해서 모두 나와 같으면 지울 표시하기
지우기(지운 개수 카운팅)
빈 곳으로 떨어지기
아래에서부터 위로
빈 공간이 있으면 그 다음 블록을 확인
빈 공간이 시작된 곳으로 이동,

'''
def solution(m, n, board):
    board = [ [board[i][j] for j in range(n)] for i in range(m)]
    check_set = set()
    result = 0
    #print(board)
    def is_same(y,x):
        v = board[y][x]
        if v == 0:
            return False
        return board[y][x+1] == v and board[y+1][x] == v and board[y+1][x+1] == v
            
        
    def check(y,x):
        nonlocal check_set
        check_set.add((y,x))
        check_set.add((y+1,x))
        check_set.add((y,x+1))
        check_set.add((y+1,x+1))
        
        
    def all_check():
        c = False
        for i in range(m-1):
            for j in range(n-1):
                # 2x2임
                if is_same(i,j):
                    check(i,j)
                    c = True
        return c
    def delete():
        nonlocal board, result
        for y,x in check_set:
            result += 1
            board[y][x] = 0
    def move():
        for j in range(n):
            for i in range(m-1, 0, -1):
                # 빈칸이면 위에 찾기
                if not board[i][j]:
                    cur = i
                    i -= 1
                    while i >= 0:
                        # 블록을 찾음
                        if board[i][j]:
                            board[cur][j] = board[i][j]
                            board[i][j] = 0
                            break
                        i -= 1
    while True:
        check_set = set()
        if not all_check():
            return result
        delete()
        move()
        # for b in board:
        #     print(b)
        # print()
        
   
    
  