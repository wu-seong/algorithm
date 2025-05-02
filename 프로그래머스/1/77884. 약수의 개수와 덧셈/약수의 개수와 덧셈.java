class Solution {
    public static boolean isAdd(int num){
        // 만약 루트한 것이 정수이면 홀수 -> 빼기
        double num_sqrt = Math.sqrt(num);
        if(num_sqrt == (int)num_sqrt){
            return false;
        }
        return true;
        
    }
    public int solution(int left, int right) {
        /*
        left - right까지 순회하면서 약수 개수 구하기
        */
        int sum = 0;
         for(int i=left; i<=right; i++){
             if(isAdd(i)){
                 sum += i;
             }
             else{
                 sum -= i;
             }
         }
        return sum;
    }
}