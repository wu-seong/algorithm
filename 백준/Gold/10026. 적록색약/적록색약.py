import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
from collections import deque

def dfs(picture,visited,node,colors):
    y,x = node
    for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        yy = dy + y
        xx = dx + x
        if 0 <= yy < N and 0 <= xx < N:
            # 방문하지 않은 지정된 색깔이면 방문
            if not visited[yy][xx] and picture[yy][xx] in colors:
                visited[yy][xx] = True
                dfs(picture,visited,(yy,xx),colors)

N = int(input().rstrip())

picture = [ [] for _ in range(N) ]
visited = [ [False for _ in range(N)] for _ in range(N)]

for i in range(N):
    picture[i] = list(input().rstrip())

# 일반인이 보는 구역의 개수
normal_cnt = 0 
# RGB 순으로 구역 찾기
for color in ('R','G','B'):
    for i in range(N):
       for j in range(N):
           # 방문하지 않은 칸 찾을 시 카운팅 및 탐색
           if picture[i][j] == color and not visited[i][j]:
               normal_cnt += 1
               visited[i][j] = True
               dfs(picture,visited,(i,j),(color))

#visited 초기화
visited = [ [False for _ in range(N)] for _ in range(N)]
# 적록색맹이 보는 구역의 개수

not_normal_cnt = 0
for colors in ( ('R','G'),('B')):
    for i in range(N):
       for j in range(N):
           # 방문하지 않은 칸 찾을 시 카운팅 및 탐색
           if picture[i][j] in colors and not visited[i][j]:
               not_normal_cnt += 1
               visited[i][j] = True
               dfs(picture,visited,(i,j),colors)


print(normal_cnt, not_normal_cnt)