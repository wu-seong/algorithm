import java.util.*;
import java.util.stream.*;
class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public int[] solution(int[] numbers) {
        /*
        이중 반복문 돌면서 Set에 넣기
        배열로 바꿔서 오름차순 정렬
        */
        Set<Integer> result = new TreeSet();
        for(int i=0; i<numbers.length; i++){
            for(int j=i+1; j<numbers.length; j++){
                result.add(numbers[i] + numbers[j]);
            }
        }
        for(int n: result){
            log(n);
        }
        return result.stream().mapToInt(i->i).toArray();
    }
}