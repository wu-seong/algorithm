class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public static boolean isNext(int num, int target){
        StringBuilder sb = new StringBuilder();
        int cnt=0;
        while(num > 0){
            int remainder = num % 2;
            if(remainder == 1){
                cnt++;
            }
            if(cnt > target){
                return false;
            }
            sb.append(remainder);
            num /= 2;
        }
        return cnt == target;
    }
    public int solution(int n) {
        /*
        개수 세고
        해당 0과 1의 개수로 만들 수 있는 모든 수 구하기
        */
        
        // 개수 세기
        int targetCnt = 0;
        String nString = Integer.toString(n,2);
        for(int i=nString.length()-1; i >= 0; i--){
            char ch = nString.charAt(i);
            if(ch == '1'){
                targetCnt++;
            }
        }
        
        while(true){
            if(isNext(++n, targetCnt)){
                return n;
            }
        }
    }
}