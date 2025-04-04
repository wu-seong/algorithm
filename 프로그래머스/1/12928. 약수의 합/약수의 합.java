import java.util.*;
class Solution {
    public int solution(int n) {
        // n 제곱근까지 로 나누면서 나누어떨어지는 수를 구한다, 젯수와 몫을 모두 약수에 추가
        
        Set<Integer> dividedSet = new HashSet<>();
        for(int i = 1; i <= Math.sqrt(n); i++){
            if(n % i == 0){
                dividedSet.add((int)n/i);
                dividedSet.add(i);
            }
        }
        System.out.println(dividedSet);
        int sum = 0;
        for(Integer num: dividedSet){
            sum += num;
        }
        return sum;
    }
}