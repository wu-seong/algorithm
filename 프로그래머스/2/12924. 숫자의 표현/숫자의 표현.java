class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public int solution(int n) {
        /*
        
        홀수이면
        3 * 5
        
        홀수로 나눈 몫이 홀수이면 가능?
        3 2 
        
        
        짝수이면 짝수로 나눈 몫이 짝수 이면
        
        4 2.5
        
        10
        
        1 2 3 = 6
        2 3 4 = 9
        
        1 2 3 4 5 6 7 8 9 10
        1 3 6 10 15 21 28 36 45 55
        
        4, 10
        
        1. n 까지의 누적합 구하기 
        2. 0 ~ n 까지 순회하면서 n 미만 까지는 pass (n이면 + 1)
        3. n 이상 부터 - 바로 이전것 부터 뺄셈 하면서 뺼셈의 결과가 n 이상이면 그만두기 (n 이면 + 1)
        */
        int[] accSum = new int[n+1];
        
        for(int i=1; i<=n; i++){
            accSum[i] = accSum[i-1] + i;
        }
        // for(int num: accSum){
        //     log(num);    
        // }
        int result = 0;
        int temp = 0;
        for(int end = 1; end <= n; end++){
            if(accSum[end] < n){
                continue;
            }
            for(int start = end - 1 ; start >= 0; start--){
                temp = accSum[end] - accSum[start];
                if(temp == n){
                    result += 1;
                }
                else if(temp > n){
                    break;
                }
            }
        }
        
        return result;
    }
}