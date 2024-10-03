def solution(n):
    # 피보나치 수를 bottom-up 방식으로 구하기, 구한 피보나치 수를 1234567로 나머지 연산하기
    dp = [0] * (n+1)
    dp[0], dp[1] = 0,1
    for i in range(2,n+1):
        dp[i] = (dp[i-1] + dp[i-2])%1234567
    return dp[n]