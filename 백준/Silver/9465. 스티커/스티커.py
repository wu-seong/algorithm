import sys

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    sticker = [ [ 0 for _ in range(n) ] for _ in range(2)]
    dp = [ [ 0 for _ in range(n)] for _ in range(2) ] 

    sticker[0] = list(map(int, input().rstrip().split()))
    sticker[1] = list(map(int, input().rstrip().split()))

    # 스티커
    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
        continue
    # 초기값 설정 (n > 2)
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    dp[0][1] = dp[1][0] + sticker[0][1]
    dp[1][1] = dp[0][0] + sticker[1][1]
    
    # 점화식
    # n-1전 다른 세로 칸 혹은 n-2의 같은 세로 칸(현재 스티커를 붙일 수 있는 경우) dp값 중 더 큰 것을 선택하여 현재 스티커 값과 더한다.
    for i in range(2,n):
        dp[0][i] = sticker[0][i] + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = sticker[1][i] + max(dp[0][i-1], dp[0][i-2])
    print(max(dp[0][n-1], dp[1][n-1]))

