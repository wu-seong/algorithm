import sys
sys.setrecursionlimit(10**6)
# 아이디어
# 방문하지 않은 점이면 카운팅하고 DFS

# 변수
# 지도 저장할 boolean 2차원 배열
# 방문 표시할 boolean 2차원 배열
# 섬 개수 카운트
def dfs(y, x):
    # 인접한 좌표 구하기
    for dy, dx in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
        yy, xx = y+dy, x+dx
        if 0 <= yy < h and 0 <= xx < w:
    # 좌표가 방문하지 않은 곳이고 섬이면 방문표시하고 재귀호출
            if not visited[yy][xx] and mmap[yy][xx]:
                visited[yy][xx] = True
                dfs(yy,xx)
input = sys.stdin.readline

while(True):
    w,h = map(int ,input().rstrip().split(" "))
    cnt = 0
    if (w,h) == (0,0):
        exit()
    mmap = [ list(map(int, input().rstrip().split(" "))) for _ in range(h)]
    #print(mmap)
    visited = [ [False for _ in range(w)] for _ in range(h)]
    #print(visited)
    for y in range(h):
        for x in range(w):
            if not visited[y][x] and mmap[y][x]:
                cnt += 1
                visited[y][x] = True
                dfs(y,x)
    print(cnt)
    
