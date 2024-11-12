from collections import deque
def solution(board):
    '''
    현재 위치가 왔던 곳이면 탐색 끝
    
    시작에서 4방향으로 미끄러지기
    
    가고자 하는 다음 곳에 장애물이나 벽이 있으면 멈추기
    
    멈춘 지점이 도착지점이면 끝
    아니면 다시 4방향으로 미끄러지기
    
    모두 탐색했는데 도착못하면 -1
    '''
    
    n,m = len(board), len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i,j)
            elif board[i][j] == 'G':
                goal = (i,j)
    result = -1
    def bfs(start):
        nonlocal result
        visited = set()
        q = deque()
        q.append((start[0], start[1], 0)) # 좌표, cnt
        visited.add(start)
        
        print(goal)
        while q:
            y, x, cnt = q.popleft()
            if (y,x) == goal:
                result = cnt
                return
            for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
                # 박을 때 까지 가기
                yy, xx = y, x
                while 0 <= yy < n and 0 <= xx < m and board[yy][xx] != 'D':
                    yy = yy + dy
                    xx = xx + dx
                yy -= dy
                xx -= dx
                if not (yy,xx) in visited:
                    visited.add((yy,xx))
                    q.append((yy,xx,cnt+1))
        
    bfs(start)
    return result