import sys

input = sys.stdin.readline

N = int(input().rstrip())
advice = [list(map(int, input().rstrip().split())) for _ in range(N)]

dp = [0] * (N + 1)

for i in range(N):
    # 이전 최대 이익값을 가져온다
    dp[i] = max(dp[i], dp[i-1])

    end = i + advice[i][0]  # 상담이 끝나는 날 

    if end <= N:
        dp[end] = max(dp[end], dp[i] + advice[i][1])

print(max(dp))
