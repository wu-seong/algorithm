import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())
i_map = [list(map(int, input().rstrip())) for _ in range(N)]

# dp 배열을 N x M x (K+1) 크기로 변경하여 방문 여부 체크
dp = [[[-1] * (K + 1) for _ in range(M)] for _ in range(N)]

def bfs():
    q = deque()
    q.append((0, 0, 0, 1))  # (y, x, 벽 부순 횟수, 이동 거리)
    dp[0][0][0] = 1  # 시작 위치 방문 처리

    while q:
        y, x, k, l = q.popleft()

        if y == N - 1 and x == M - 1:  # 목표 지점 도달
            return l

        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            yy, xx = y + dy, x + dx
            if 0 <= yy < N and 0 <= xx < M:
                if i_map[yy][xx] == 0 and dp[yy][xx][k] == -1:
                    # 벽이 아니고 방문한 적이 없을 때
                    dp[yy][xx][k] = l + 1
                    q.append((yy, xx, k, l + 1))

                elif i_map[yy][xx] == 1 and k < K and dp[yy][xx][k + 1] == -1:
                    # 벽이지만 부술 수 있고, 해당 벽을 부순 경우 방문한 적이 없을 때
                    dp[yy][xx][k + 1] = l + 1
                    q.append((yy, xx, k + 1, l + 1))

    return -1  # 목표 지점 도달 불가능

print(bfs())
