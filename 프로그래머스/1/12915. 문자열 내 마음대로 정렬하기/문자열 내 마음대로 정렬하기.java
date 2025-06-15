import java.util.*;
class Solution {
    public String[] solution(String[] strings, int n) {
        /*
        String배열 sort
        comparator x -> x[n]
        */
        Arrays.sort(strings, (s1, s2) -> {
            if(s1.charAt(n) == s2.charAt(n)){
                return s1.compareTo(s2);
            }
            return s1.charAt(n) - s2.charAt(n);
        });
        return strings;
    }
}