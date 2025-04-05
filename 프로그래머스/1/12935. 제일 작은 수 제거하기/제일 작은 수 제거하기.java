import java.util.*;

class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public int[] solution(int[] arr) {
        // arr를 순회하면서 최솟값을 찾기 만약 같다면 계속 채워넣기 
        final int min = Arrays.stream(arr)
            .min()
            .getAsInt();
        
        int[] removedArray = Arrays.stream(arr)
            .filter(num -> num != min)
            .toArray();
        for(int num: removedArray){
            log(num);   
        }
        
        return removedArray.length == 0 ? new int[]{-1} : removedArray;
    }
}