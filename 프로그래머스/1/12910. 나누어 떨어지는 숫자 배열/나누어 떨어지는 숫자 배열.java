import java.util.*;
import java.util.stream.*;

class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public int[] solution(int[] arr, int divisor) {
        List<Integer> filteredList = new ArrayList<>();
        for(int num: arr){
            if(num % divisor == 0){
                filteredList.add(num);
            }
        }
        Collections.sort(filteredList);
        log(filteredList);
        return filteredList.isEmpty() 
            ? new int[]{-1} 
            : filteredList.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}