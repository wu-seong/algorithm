'''
목표지점에서 BFS 하면서 level 체크하기
1. 입력 배열로 받기
2. 시작점 2 찾기
3. BFS 하기
    시작 지점 넣기
    시작 지점 방문 체크 = 0으로 만들기

    큐에서 다음 방문할 위치 꺼내기
    꺼내서 해당 위치에 level 저장

    상하좌우 0이 아니면 인큐
'''

import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().rstrip().split())

r_map = [] * n
for _ in range(n):
    r_map.append(list(map(int, input().rstrip().split())))
#print(r_map)

cost = [[0 for _ in range(m)] for _ in range(n)]
start = -1
for i in range(n):
    for j in range(m):
        if r_map[i][j] == 2:
            start = (i,j)


visited = set()

def bfs(start):
    q = deque()
    s_y, s_x = start
    q.append((s_y, s_x, 0))
    visited.add((s_y, s_x))
    
    while q:
        y, x, l = q.popleft()
        cost[y][x] = l
        for dy, dx in [(1,0), (0,1), (-1,0), (0,-1)]:
            yy = y + dy
            xx = x + dx
            if 0 <= yy < n and 0 <= xx < m and r_map[yy][xx] and not (yy,xx) in visited :
                visited.add((yy, xx))
                q.append((yy, xx, l+1))
bfs(start)

for i in range(n):
    for j in range(m):
        if r_map[i][j] and not (i,j) in visited: # 지도 상으로 존재하는 위치인데 못간 경우
            cost[i][j] = -1

for i in range(n):
    cost[i] = list(map(str, cost[i]))
    print(" ".join(cost[i]))