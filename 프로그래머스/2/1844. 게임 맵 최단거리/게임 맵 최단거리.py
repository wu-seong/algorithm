'''
최단거리 문제
bfs를 통해 해당 좌표에 도달 시 depth를 구한다.

캐릭터는 항상 (0,0) 목적지는 (n-1,m-1)

'''
from collections import deque
def solution(maps):
    n,m = len(maps), len(maps[0])
    #print(n,m)
    def bfs(start):
        visited = set()
        queue = deque()
        # 갈 곳을 queue에 넣는다.
        queue.append((0,0,1))
        visited.add((0,0))
        while queue:
            y,x,d = queue.popleft()
            if (y,x) == (n-1,m-1):
                return d
            for dy, dx in [(0,1),(1,0),(-1,0),(0,-1)]:
                yy = y + dy
                xx = x + dx
                if 0 <= yy < n and 0 <= xx < m and maps[yy][xx] == 1:
                    if (yy,xx) not in visited:
                        queue.append((yy,xx,d+1))
                        visited.add((yy,xx))
        return -1
            
        # queue에서 popleft한다.
        # 해당 지점 방문 여부 판단하여 방문 안했을 시에만 다음 갈 곳 queue에 넣기
    
    return bfs((0,0))
    