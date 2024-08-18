def solution(triangle):
    N = len(triangle)
    max_sum = 0
    dp = [ [ 0 for _ in range(i)] for i in range(1,N+1)]
    dp[0][0] = triangle[0][0]
    if N == 1:
        return dp[0][0]
    for i in range(1,N):
        dp[i][0] = triangle[i][0] + dp[i-1][0]
        dp[i][-1] = triangle[i][-1] + dp[i-1][-1]
        max_sum = max(max_sum, dp[i][0],dp[i][-1])
        for j in range(1,i):
            dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
            max_sum = max(max_sum, dp[i][j])
    answer = max_sum
    return answer