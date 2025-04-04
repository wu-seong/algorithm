import java.util.*;

public class Solution {
    public int solution(int n) {
        String nString = String.valueOf(n);
        int sum = 0;
        for (int i = 0; i < nString.length(); i++){
            // System.out.println(Character.getNumericValue(nString.charAt(i)));
            sum += Character.getNumericValue(nString.charAt(i));
        }
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        return sum;
    }
}