import java.util.*;
class Solution {
    public int solution(int[] d, int budget) {
        /*
        정렬 후에 누적합
        buget이 누적합보다 크면 카운팅 작으면 끝
        */
        Arrays.sort(d);
        int sum = 0;
        int result = 0;
        for(int i=0; i<d.length ;i++){
            sum += d[i];
            if(sum > budget){
                return i;
            }
        }
        return d.length;
    }
}