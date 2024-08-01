import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 3 4 5
# 3 2
# 2 2
# 3 1
# 2 3
# 1 1
# 0 = 통로, 1 = 음식물
def dfs(trash, node, visited):
    global size
    y,x = node
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        xx = dx+x
        yy = dy+y
        if 1 <= xx <= M and 1 <= yy <= N:
            if not visited[yy][xx] and trash[yy][xx] == 1:
                size += 1
                visited[yy][xx] = True
                dfs(trash, (yy,xx), visited) 
N,M,K = map(int, input().rstrip().split())

trash = [ [0 for _ in range(M+1)] for i in range(N+1)]
visited = [ [False for _ in range(M+1)] for i in range(N+1)]
trash_list = []
# 음쓰 정보 저장
for i in range(K):
    r,c = map(int, input().rstrip().split())
    trash[r][c] = 1
    trash_list.append((r,c))

# 음쓰 크기 탐색하며 계산
max_size = 0
for t in trash_list:
    r,c = t
    # 탐색하지 않은 음쓰면 탐색
    if not visited[r][c]:
        size = 1
        visited[r][c] = True
        dfs(trash,(r,c),visited)
        if size > max_size:
            max_size = size
print(max_size)

