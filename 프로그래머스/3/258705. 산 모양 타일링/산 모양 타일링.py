def solution(n, tops):
    answer = 0
    dp = [1] * ((2*n)+2)
    for i in range(2,(2*n)+2):
        dp[i] = dp[i-1] + dp[i-2]
        if i % 2 == 0 and tops[int(i//2)-1]  ==  1:
            dp[i] += dp[i-1]
        dp[i] %= 10007
    #print(dp)
    #print(dp[-1]%10007)
    return(dp[-1]) 

# 0 - 1
# 1 - 1
# 2 - dp[n-1] + dp[n-2] + option(dp[n] + dp[n-1])
# 3 - dp[n-1] + dp[n-2]
# 4 - dp[n-1] + dp[n-2] + option(dp[n] + dp[n-1])