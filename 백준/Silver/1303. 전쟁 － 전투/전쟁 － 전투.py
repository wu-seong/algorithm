import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# 5 5
# WBWWW
# WWWWW
# BBBBB
# BBBWW
# WWWWW
def dfs(color, war, node, visited):
    global area
    y,x = node
    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        xx = dx+x
        yy = dy+y
        if 0 <= yy < N and 0 <= xx < M:
            if not visited[yy][xx] and war[yy][xx] == color:
                visited[yy][xx] = True
                area += 1
                dfs(color,war,(yy,xx),visited)

M,N = map(int, input().rstrip().split())

visited = [ [False for _ in range(M)] for _ in range(N)]
war = [ list((input().rstrip())) for _ in range(N)]
# W만 기준으로 탐색, 한 인접요소 구한 뒤 구역수 제곱
# 반복 후 제곱 수 더하기
w_total_power = 0
for i in range(N):
    for j in range(M):
        if war[i][j] == 'W' and not visited[i][j]:
            area = 1
            visited[i][j] = True
            dfs('W',war,(i,j),visited)
            power = area**2
            w_total_power += power

# 탐색 하면서 그래프 바뀌는가? -> x, 그대로 사용가능
# vsited 초기화, B기준으로 동일하게
visited = [ [False for _ in range(M)] for _ in range(N)]
b_total_power = 0
for i in range(N):
    for j in range(M):
        if war[i][j] == 'B' and not visited[i][j]:
            area = 1
            visited[i][j] = True
            dfs('B',war,(i,j),visited)
            power = area**2
            b_total_power += power
        
print(w_total_power, b_total_power)
