import sys
sys.setrecursionlimit(10**6)
'''
모든 석유 영역에 대해서 bfs하면서 크기를 구하고 해당 석유 위치에 id마킹을 한다.

'''
from collections import deque
def solution(land):
    n,m = len(land), len(land[0])
    area = [[0 for _ in range(m)] for _ in range(n)]
    size = {}
    id = 1
    def bfs(sy, sx):
        nonlocal area, id
        if not land[sy][sx] or area[sy][sx]:
            return
        q = deque()
        area[sy][sx] = id
        cnt = 0
        q.append((sy,sx))
        while q:
            y,x = q.popleft()
            cnt += 1
            
            for dy ,dx in [(1,0),(0,1),(-1,0),(0,-1)]:
                yy, xx = y+dy, x+dx
                if 0 <= yy < n and 0 <= xx < m and land[yy][xx] and not area[yy][xx]:
                    area[yy][xx] = id
                    q.append((yy,xx))
        size[id] = cnt
        id += 1
        
    for i in range(n):
        for j in range(m):
            bfs(i,j)
        
    # for a in area:
    #     print(a)
    # print(size)
    
    result = 0
    for i in range(m): # 내려가면서 어떤 영역들이 존재하는지 찾기
        areas = set()
        for j in range(n):
            if area[j][i]:
                areas.add(area[j][i])
        sum = 0
        for a in areas:
            sum += size[a]
        result = max(result, sum)
    print(result)
    return result
    
            
    
    