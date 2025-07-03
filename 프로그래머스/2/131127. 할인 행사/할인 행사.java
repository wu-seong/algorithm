import java.util.*;

class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public int solution(String[] want, int[] number, String[] discount) {
        /*
        최초에 want*number의 길이 만큼 discount를 돌면서
        count를 감소시킨다. (want와 무관한 것이면 pass)
        만약 count 중 0보다 큰 것이 있다면 해당 다음날로 넘어간다.
        하루씩 이동하면서 start는 빼고 end를 더한다.
        가능한 날이 없으면 0을 반환한다.
        */
        Map<String, Integer> count = new HashMap<>();
        // count 초기화
        int n = want.length;
        int total = 0;
        for(int i=0; i<n; i++){
            String key = want[i];
            Integer value = number[i];
            total += value;
            count.put(key, value);
        }
        //log(count);
        
        int result = 0;
        // 첫 시뮬
        for(int i=0; i<total; i++){
            String key = discount[i];
            if(count.containsKey(key)){
                int cnt = count.get(key);
                count.put(key, cnt - 1);
            }
        }
        boolean zero = true;
        for(String key: count.keySet()){
            if(count.get(key) != 0){
                zero = false;
                break;
            }
        }
        if(zero){
            result += 1;
        }
        for(int i=0; i+total<discount.length; i++){
            String startKey = discount[i];
            String endKey =  discount[i+total];
            if(count.containsKey(startKey)){
                count.put(startKey, count.get(startKey) + 1);
            }
            if(count.containsKey(endKey)){
                count.put(endKey, count.get(endKey) - 1);
            }
            // 검증
            zero = true;
            for(String key: count.keySet()){
                if(count.get(key) != 0){
                    zero = false;
                    break;
                }
            } 
            //log(count);
            if(zero){
                result += 1;
            }
        }
        return result;
    }
}