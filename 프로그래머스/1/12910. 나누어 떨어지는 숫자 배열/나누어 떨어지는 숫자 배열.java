import java.util.*;
import java.util.stream.*;

class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public int[] solution(int[] arr, int divisor) {
        int[] filteredArr = Arrays.stream(arr)
            .filter(n -> n % divisor == 0)
            .toArray();
        Arrays.sort(filteredArr);
        
        return filteredArr.length == 0 
            ? new int[]{-1} 
            : filteredArr;
    }
}