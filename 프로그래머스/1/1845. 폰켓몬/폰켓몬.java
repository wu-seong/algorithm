import java.util.*;
import java.util.stream.*;

class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public int solution(int[] nums) {
        int N = nums.length;
        // set으로 바꾸기
        Set<Integer> pIndex = Arrays.stream(nums)
            .boxed()
            .collect(Collectors.toSet());
        for(Integer index: pIndex){
            log(index);
        }
        // max(n/2 or set length)
        int typeCnt = pIndex.size();
        if(typeCnt > N/2){
            return N/2;
        }
        return typeCnt;
    }
}