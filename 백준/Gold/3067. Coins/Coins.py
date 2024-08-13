import sys
input = sys.stdin.readline

T = int(input().rstrip())

for i in range(T):
    N = int(input().rstrip())
    coins = list(map(int,input().rstrip().split()))
    M = int(input().rstrip())

    dp = [ [ 0 for _ in range(M+1)] for _ in range(N)]
    # 첫번째 선택한 코인으로 만들 수 있는 경우
    for i in range(1,M+1):
        if i % coins[0] == 0:
            dp[0][i] = 1
    # n번째 선택한 코인으로 만들 수 있는 경우 (n > 1)
    for i in range(1,N):
        for j in range(1,M+1):
            if j < coins[i]:
                dp[i][j] = dp[i-1][j]
            elif j == coins[i]: 
                dp[i][j] = 1 + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]

    print(dp[N-1][M])