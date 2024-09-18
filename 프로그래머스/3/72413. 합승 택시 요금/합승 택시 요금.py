
def solution(n, s, a, b, fares):
    dp = [[ float('inf') for _ in range(n)] for _ in range(n)]
    for u,v,w in fares:
        dp[u-1][v-1] = w
        dp[v-1][u-1] = w
    for i in range(n):
        dp[i][i] = 0
    #print(dp)
    for k in range(n):
        for start in range(n):
            for end in range(n):
                dp[start][end] = min(dp[start][end], dp[start][k] + dp[k][end])
    #print(dp)
    min_cost = float('inf')
    for i in range(n):
        min_cost = min(min_cost, dp[s-1][i] + dp[i][a-1] + dp[i][b-1])
    #print(min_cost)
    return min_cost