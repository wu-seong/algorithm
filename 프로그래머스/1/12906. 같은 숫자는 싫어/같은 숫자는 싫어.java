import java.util.*;

public class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public int[] solution(int[] arr) {
        // 배열의 시작부터 순회하면서 스택에 push
        // 만약 peek한 값과 같으면 push하진 않음
        Stack<Integer> stack = new Stack();
        for(int num: arr){
            if(stack.isEmpty() || stack.peek() != num){
                stack.push(num);
            }
        }
        int[] result = stack.stream()
            .mapToInt(x -> x)
            .toArray();
        // for(int num: result){
        //     log(num);
        // }
        return result;
    }
}