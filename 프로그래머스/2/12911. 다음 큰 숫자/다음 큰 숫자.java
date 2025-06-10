class Solution {
    public int solution(int n) {
        /*
        더 큰 수 중 이진변환해서 숫자 1 카운팅해서 ~하기
        */
        String binary_n = Integer.toString(n, 2);
        int targetCnt = 0;
        for(char ch: binary_n.toCharArray()){
            if(ch == '1'){
                targetCnt++;
            }
        }
        //System.out.println(targetCnt);
        int cnt;
        while(true){
            cnt = 0;
            binary_n = Integer.toString(++n, 2);
            for(char ch: binary_n.toCharArray()){
                if(ch == '1'){
                    cnt++;
                }
            }
            if(cnt == targetCnt){
                return n;
            }
        }
    }
}