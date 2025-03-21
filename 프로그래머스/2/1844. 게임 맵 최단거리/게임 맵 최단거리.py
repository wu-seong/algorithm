'''
bfs해서 n,m에 도착하면 해당 level을 반환 만약 도착하지 못하고 queue가 종료되면 -1반환
'''
from collections import deque

def solution(maps):
    n,m = len(maps), len(maps[0])
    visited = set()
    q = deque()
    
    visited.add((0,0))
    q.append((0,0,1))
    
    while q:
        y,x,l = q.popleft()
        if (y,x) == (n-1,m-1):
            return l
        for dy, dx in [(1,0),(0,1),(-1,0),(0,-1)]:
            yy,xx = y+dy, x+dx
            if 0 <= yy < n and 0 <= xx < m and maps[yy][xx] == 1:
                if not (yy,xx) in visited:
                    visited.add((yy,xx))
                    q.append((yy,xx,l+1))
    return -1
                