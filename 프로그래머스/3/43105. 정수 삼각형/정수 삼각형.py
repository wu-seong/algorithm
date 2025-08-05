def solution(triangle):
    '''
    max(왼쪽위에서의 최적값, 오른쪽 위에서의 최적값)
    오른쪽 위의 최적값 = row - 1, col
    왼쪽 위의 최적값 = row - 1, col - 1 (col > 0)
    
    
    '''
    n = len(triangle)
    dp = [[0 for _ in range(i+1)] for i in range(n)]
    dp[0][0] = triangle[0][0]
    print(dp[0])
    for i in range(1,n):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
            #print(dp[i])
    return max(dp[n-1])
    