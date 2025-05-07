class Solution {
    public int solution(int[] number) {
        /*
        브루트 포스 다 해보기
        */
        int result = 0;
        int n = number.length;
        for(int i=0; i<n;i++){
            int sum = number[i];
            for(int j=i+1; j<n;j++){
                sum += number[j];
                for(int k=j+1; k<n; k++){
                    sum += number[k];
                    if(sum == 0){
                        result += 1;
                    }
                    sum -= number[k];
                }
                sum -= number[j];
            }
        }
        return result;
    }
}