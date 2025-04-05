import java.util.*;

class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public int solution(int[] numbers) {
        Set<Integer> all = new HashSet<>(Arrays.asList(0,1,2,3,4,5,6,7,8,9));
        // log(numSet);
        List<Integer> numList = new ArrayList<>();
        for(int num: numbers){
            numList.add(num);
        }
        Set<Integer> numSet = new HashSet<>(numList);
        all.removeAll(numSet);
        // log(all);
        int sum = 0;
        for(int num: all){
            sum += num;
        }
        return sum;
    }
}