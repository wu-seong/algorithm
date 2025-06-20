class Solution {
    public long solution(int n) {
        /*
        dp문제
        dp[0] = 1
        dp[1] = 1
        dp[2] = dp[1] + dp[0] 2
        3 -> 3
        4 -> 5
        ...
        (n>1)dp[n] = dp[n-1] + dp[n-2]
        */
        long[] dp = new long[n+1];
        dp[0] = 1;
        dp[1] = 1;
        for(int i=2; i<=n; i++){
            dp[i] = (dp[i-1] + dp[i-2])%1234567;
        }
        return dp[n];
    }
}