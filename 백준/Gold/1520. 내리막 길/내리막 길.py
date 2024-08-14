import sys
from collections import deque
input = sys.stdin.readline


# start -> end까지 경로의 수 구해서 저장하는 함수
def a(start):
    y,x = start
    cnt = 0
    for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        yy = y + dy
        xx = x + dx
        if  0<= yy < M and 0 <= xx < N:
            # 내리막길 이면 구하기
            if m[yy][xx] < m[y][x]:
                # 구하지 않았으면 구하기
                if dp[yy][xx] == -1:
                    a((yy,xx))
                    cnt += dp[yy][xx]
                # 이미 구했으면 가져오기
                else:
                    cnt += dp[yy][xx]
    dp[y][x] = cnt

M,N = map(int,input().rstrip().split())

dp = [ [ -1 for _ in range(N)] for _ in range(M)]
dp[-1][-1] = 1
m = [ list(map(int, input().rstrip().split())) for _ in range(M)]
a((0,0))
print(dp[0][0])
