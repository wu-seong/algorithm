class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public String solution(String s) {
        StringBuilder jadenCase = new StringBuilder();
        int n = s.length();
        int i = 0;
        boolean firstReady = true;
        while(i<n){
            //이전이 공백문자
            char cur = s.charAt(i);
            // log(i + "번째: "+ firstReady);
            if(firstReady){
                if(cur == ' '){
                    jadenCase.append(cur);
                }
                else if(cur <= 'z' && cur >= 'a'){
                    jadenCase.append((char)(cur - 32));
                    firstReady = false;
                }
                else{
                    firstReady = false;
                    jadenCase.append(cur);
                }
            }
            //단어 진행중
            else{
                if(cur == ' '){
                    jadenCase.append(cur);
                    firstReady = true;
                }
                else if(cur >= 'A' && cur <= 'Z'){
                    jadenCase.append((char)(cur + 32));
                }
                else{
                    jadenCase.append(cur);
                }
            }
            i += 1;
        }
        log(jadenCase);
        return jadenCase.toString();
    }
}