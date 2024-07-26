import sys
from collections import deque

input = sys.stdin.readline

dm = (1, -1, 0, 0, 0, 0)
dn = (0, 0, 1, -1, 0, 0)
dh = (0, 0, 0, 0, 1, -1)
M, N, H = map(int, input().rstrip().split())

tomato = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

queue = deque()
for h in range(H):
    for n in range(N):
        tomato[h][n] = list(map(int, input().rstrip().split()))
        for m in range(M):
            if tomato[h][n][m] == 1:
                queue.append((h, n, m, 0))  # 익은 토마토를 큐에 추가

max_days = 0
while queue:
    h, n, m, days = queue.popleft()
    for i in range(6):
        nh = h + dh[i]
        nn = n + dn[i]
        nm = m + dm[i]
        if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
            if not visited[nh][nn][nm] and tomato[nh][nn][nm] == 0:
                visited[nh][nn][nm] = True
                tomato[nh][nn][nm] = 1  # 토마토를 익힘
                queue.append((nh, nn, nm, days + 1))
                max_days = max(max_days, days + 1)

# 익지 않은 토마토가 있는지 확인
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 0:
                print("-1")
                exit()

print(max_days)
