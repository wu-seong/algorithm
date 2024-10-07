def solution(n):
    # dp
    # 첫번째 칸으로 가는 경우 1
    # 두번째 칸 2
    # 세번째 칸부터는 dp[i] = dp[i-1] + dp[i-2]
    dp = [0]*n
    if n < 3:
        return n
    dp[0] = 1
    dp[1] = 2
    for i in range(2,n):
        dp[i] = (dp[i-1] + dp[i-2])%1234567
    return dp[n-1]