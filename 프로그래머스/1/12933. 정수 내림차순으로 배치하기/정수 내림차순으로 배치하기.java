import java.util.*;
class Solution {
    public long solution(long n) {
        String str = String.valueOf(n);
        char[] arr = str.toCharArray();
        //System.out.println(arr);
        Arrays.sort(arr);
        str = new String(arr);
        str = new StringBuilder(str).reverse().toString();
        return Long.parseLong(str);
    }
}