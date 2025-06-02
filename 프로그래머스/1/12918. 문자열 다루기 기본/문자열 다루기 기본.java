class Solution {
    public boolean solution(String s) {
        /*
        길이 check
        숫자 check
        */
        
        if(!(s.length() == 4 || s.length() == 6)){
            return false;
        }
        for(char ch: s.toCharArray()){
            if(ch < '0' || ch > '9'){
                return false;
            }
        }
        return true;
    }
}