'''
시작점에서 각 위치마다의 거리를 저장하는 맵
도착점에서 각 위치마다의 거리를 저장하는 맵
따로 구하고

시작점에서 도착점까지의 거리를 최단거리로 저장, 불가능하면 -1 

벽에 대해서 순회하며 각 맵에서 상하좌우 중 가장 작은 값의 합 + 1으로 최단거리를 갱신한다.
'''
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int, input().rstrip().split())
m_map = []
for _ in range(N):
    m_map.append(list(map(int,(input().rstrip()))))
#print(m_map)

def bfs(start, m):
    visited = set()
    q = deque()
    s_y, s_x = start
    q.append((s_y, s_x, 1))
    visited.add((s_y,s_x))
    while q:
        y, x, l = q.popleft()
        m[y][x] = l
        for dy ,dx in [(1,0), (0,1), (-1,0), (0,-1)]:
            yy = y + dy
            xx = x + dx
            if 0 <= yy < N and 0 <= xx < M and not (yy,xx) in visited:
                if not m_map[yy][xx]:
                    visited.add((yy,xx))
                    q.append((yy, xx, l+1))
s_map = [ [1e6 for _ in range(M)] for _ in range(N)]
e_map = [ [1e6 for _ in range(M)] for _ in range(N)]
bfs((0,0), s_map)
bfs((N-1, M-1), e_map)
# for m in e_map:
#     print(m)
result = s_map[N-1][M-1]

for y in range(N):
    for x in range(M):
        if m_map[y][x]:
            s_min, e_min = 1e9, 1e9
            for dy ,dx in [(1,0), (0,1), (-1,0), (0,-1)]:
                yy = y + dy
                xx = x + dx
                if 0 <= yy < N and 0 <= xx < M:
                    s_min = min(s_min, s_map[yy][xx])
                    e_min = min(e_min, e_map[yy][xx])
            result = min(result, s_min + e_min + 1)
            #print("y,",y, "x", x, ":", result)
if result == 1e6:
    print(-1)
else:
    print(result)