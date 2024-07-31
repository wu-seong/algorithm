import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
print = sys.stdout.write

dx = (0,0,1,-1)
dy = (1,-1,0,0)

def dfs(paper, visited, node):
    global area
    y,x = node
    for i in range(4):
        next_x = x+dx[i]
        next_y = y+dy[i]
        if 0 <= next_x < N and 0 <= next_y < M:
            if not paper[next_y][next_x] and not visited[next_y][next_x]:
                area += 1
                visited[next_y][next_x] = True
                dfs(paper, visited, (next_y,next_x))
                
M,N,K = map(int, input().rstrip().split())

# 입력 받아 직사각형 내부 표시하기
paper = [ [False for _ in range(N)] for _ in range(M)]
visited = [ [False for _ in range(N)] for _ in range(M)]
area_list = []

for i in range(K):
    start_x,start_y, end_x,end_y = map(int, input().rstrip().split())
    for m in range(start_y,end_y):
        for n in range(start_x, end_x):
            paper[m][n] = True
# for i in range(M):
#     print(paper[i])
        
# 모눈종이 순회하며 분리된 영역 찾기
cnt = 0
for m in range(M):
    for n in range(N):
        if not paper[m][n] and not visited[m][n]:
            visited[m][n] = True
            cnt += 1
            area = 1
            dfs(paper,visited,(m,n))
            area_list.append(area)

# 영역 찾았으면 dfs로 탐색하며 넓이 카운팅하기

# 모눈종이를 모두 순회할 때까지 영역도 카운팅
print("%d\n" %cnt)
area_list.sort()
for area in area_list:
    print("%d " %area)
print("\n")