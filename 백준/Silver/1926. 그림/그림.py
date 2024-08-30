import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().rstrip().split())
board = [ list(map(int, input().rstrip().split())) for _ in range(n)]
# 그림 찾기
p_cnt = 0
max_area = 0
visited = [[False for _ in range(m)] for _ in range(n)] 
for i in range(n):
    for j in range(m):
        area = 0
        if board[i][j] == 1 and not visited[i][j]: 
            p_cnt += 1
        # 그래프 탐색
            queue = deque()
            visited[i][j] = True
            queue.append((i,j))
            while queue:
                y,x= queue.popleft()
                area += 1
                for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
                    yy = y + dy
                    xx = x + dx
                    if 0 <= yy < n and 0 <= xx < m:
                        if not visited[yy][xx] and board[yy][xx] == 1:
                            visited[yy][xx] = True
                            queue.append((yy,xx))
        max_area = max(max_area, area)
print(p_cnt, max_area)
