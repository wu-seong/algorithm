class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public String solution(String s, int n) {
        /*
        1. 모두 대문자로 만든다.
        2. 'A' 만큼 뺀다 0 - 25
        3. n만큼 밀고 26으로 나눈다
        4. 다시 'A만큼 더한다'
        5. 원본을 보면서 대소문자 복구한다.
        */
        StringBuilder us = new StringBuilder(s);
        //log(us);
        for(int i=0; i<us.length(); i++){
            char c = us.charAt(i);
            if(Character.isAlphabetic(c)){
                char dist = Character.isUpperCase(c) ? 'A' : 'a';
                us.setCharAt(i, (char)( ( (c -dist + n) % 26) + dist));
            }
        }
        //log(us);
        return us.toString();
    }
}