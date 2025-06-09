class Solution {
    public String solution(String s) {
        /*
        문자열 순회하면서 공백이 아니면 짝홀수 시작, 공백이면 단어 끝
        */
        StringBuilder sb = new StringBuilder();
        boolean pair = true;
        for(char ch: s.toCharArray()){
            if(ch == ' '){
                pair = true;
                sb.append(ch);
                continue;
            }
            if(pair){
                if('a' <= ch && ch <= 'z'){
                    sb.append((char)(ch - 32));
                }
                else{
                    sb.append(ch);
                }
                pair = false;
            }
            else{
                if('A' <= ch && ch <= 'Z'){
                    sb.append((char)(ch + 32));
                }
                else{
                    sb.append(ch);
                }
                pair = true;
            }
        }
        return sb.toString();
    }
}