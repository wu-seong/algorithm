
def solution(land):
    # dp 각 땅을 밟을 때의 최댓값을 구한다.
    # 각 땅을 밟을 때 현재와 겹치는 것은 제외시킨다.
    n = len(land)
    dp = [[0,0,0,0] for i in range(n)]
    dp[0] = land[0]
    for i in range(1,n): 
        for j in range(4): # 하나의 땅마다 최적값 구하기
            max_dp = 0
            for k in range(4): # 현재 연속된 땅 제외 이전땅 중 최적값 찾기
                if k != j:
                    max_dp = max(max_dp, dp[i-1][k])
            cur_value = land[i][j]
            dp[i][j] = cur_value + max_dp
    return max(dp[n-1])