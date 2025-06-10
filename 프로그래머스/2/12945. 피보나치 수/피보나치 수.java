class Solution {
    public int solution(int n) {
        /*
        바텀 업 방식으로 피보나치 수 배열에 저장하기(1234567로 나머지 연산)
        */
        int[] dp = new int[n+1];
        dp[0] = 0;
        dp[1] = 1;
        for(int i=2; i<=n; i++){
            dp[i] = (dp[i-1] + dp[i-2]) % 1234567;
        }
        return dp[n];
    }
}