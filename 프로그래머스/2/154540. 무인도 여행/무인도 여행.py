from collections import deque
def solution(maps):
    '''
    숫자를 찾기
    BFS 하면서 숫자 합 구해서 결과에 넣기
    모든 지도를 다 돌 때 까지 반복
    다돌았는데 한번도 숫자가 없으면 -1
    '''
    def bfs(i,j,cnt):
        q = deque()
        q.append((i, j, cnt)) 
        visited.add((i,j))
        sum = 0
        while q:
            y, x, c = q.popleft()
            sum += int(c)
            for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
                yy = y + dy
                xx = x + dx
                if 0 <= yy < n and 0 <= xx < m:
                    if not (yy,xx) in visited and maps[yy][xx] != 'X':
                        q.append((yy,xx,maps[yy][xx]))
                        visited.add((yy,xx))
        result.append(sum)
        
    visited = set()
    n,m = len(maps), len(maps[0])
    result = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X':
                if not (i,j) in visited:
                    bfs(i,j,maps[i][j])
    if result:
        result.sort()
        return result
    return [-1] 