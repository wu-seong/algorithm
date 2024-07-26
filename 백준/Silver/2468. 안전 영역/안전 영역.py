import sys

input = sys.stdin.readline
print = sys.stdout.write

from collections import deque

N = int(input().rstrip())

h_map = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1):
    h_map[i] = list(map(int, input().rstrip().split()))
    h_map[i].insert(0,0)
queue = deque()

max = 0
#print("%s\n" %h_map)
# 빗물의 높이 0 ~ 100 반복
for r_height in range(0, 101):
    visited = [[False for _ in range(N+1)] for _ in range(N+1)]
    cnt = 0
    # 빗물의 높이 마다 각 지점의 안전 여부를 확인
    for i in range(1, N+1):
        for j in range(1, N+1):
            # 지점이 침수 지역이거나 이미 탐색한 지역이이면 탐색하지 않음
            #print("i:%d j:%d\n" %(i,j))
            if h_map[i][j] <= r_height or visited[i][j]:
                continue
            # 아닐 시에 카운트하고 탐색 시작
            cnt += 1
            visited[i][j] = True
            root = (i,j)
            queue.append(root)
            while queue:
                r,c = queue.popleft()
                #print("%d %d" %(r,c))
                if c+1 <= N and not visited[r][c+1] and h_map[r][c+1] > r_height:
                    visited[r][c+1] = True
                    queue.append((r,c+1))
                if c-1 >= 1 and not visited[r][c-1] and h_map[r][c-1] > r_height:
                    visited[r][c-1] = True
                    queue.append((r,c-1))
                if r+1 <= N and not visited[r+1][c] and h_map[r+1][c] > r_height:
                    visited[r+1][c] = True
                    queue.append((r+1,c))
                if r-1 >= 1 and not visited[r-1][c] and h_map[r-1][c] > r_height:
                    visited[r-1][c] = True
                    queue.append((r-1,c)) 
    #print("r_h:%d cnt:%d\n" %(r_height, cnt))
    if cnt > max:
        max = cnt
print("%d\n" %max)
