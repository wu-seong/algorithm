import java.util.*;

public class Solution {
    public int solution(int n) {
        /*
        짝수 마다 이전의 더 최적의 길이 있기 때문에 k로는 1 초과해서 움직일 상황이 없다.
        N을 2로 나누고 안나누어 떨어질 때는 -1하고 카운팅
        N이 0이 될 때 까지
        */
        int cnt=0;
        while(n>0){
            if(n%2 == 0){
                n /= 2;
            }
            else{
                n -= 1;
                cnt += 1;
            }
        }
        return cnt;
    }
}