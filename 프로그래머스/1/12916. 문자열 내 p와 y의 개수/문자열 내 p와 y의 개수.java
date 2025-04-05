class Solution {
    boolean solution(String s) {
        int pCnt = 0, yCnt = 0;
        for(char c: s.toCharArray()){
            if(c == 'y' || c == 'Y'){
                yCnt += 1;
            }
            if(c == 'p' || c =='P'){
                pCnt += 1;
            }
        }
        return yCnt == pCnt;
    }
}