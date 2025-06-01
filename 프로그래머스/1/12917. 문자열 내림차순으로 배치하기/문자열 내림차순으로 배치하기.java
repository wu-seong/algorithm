import java.util.*;
class Solution {
    public String solution(String s) {
        /*
        큰 것부터 작은 것 순
        문자열 반대 정렬
        */
        
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        StringBuilder sb = new StringBuilder(new String(chars));
        String result = sb.reverse().toString();
        return result;
    }
}