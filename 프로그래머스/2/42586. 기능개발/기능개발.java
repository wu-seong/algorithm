import java.util.*;

class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public int[] solution(int[] progresses, int[] speeds) {
        // 각 기능마다 걸리는 시간을 구하기
        // 남은 작업률을 속도로 나눈 몫 -> 일 수 + 1
        // 나머지가 없으면 몫 자체가 일 수
        
        // 5 10 1 1 20 1
        // 5 10 
        // stack에 첫 녀석 저장
        // top 보다 작거나 같으면 카운팅하기
        // 더 크면 stack에 넣고 카운팅 저장하기
        int n = progresses.length;
        int[] delay = new int[n];
        for(int i = 0; i<n; i++){
            int remain = 100 - progresses[i];
            if(remain % speeds[i] == 0){
                delay[i] = remain / speeds[i];
            }
            else{
                delay[i] = remain / speeds[i] + 1;
            }
        }
        
        // for(int num: delay){
        //     log(num);
        // }
        
        Stack<Integer> stack = new Stack();
        List<Integer> result = new ArrayList<>();
        int cnt = 0;
        for(int i=0; i<n; i++){
            // stack에 저장하고 카운팅
            if(stack.isEmpty()){
                cnt += 1;
                stack.push(delay[i]);
                continue;
            }
            // 더 큰 녀석이 나오면 지금까지 했던 것 저장하고 스택에 push
            if(stack.peek() < delay[i]){
                result.add(cnt);
                cnt = 1;
                stack.push(delay[i]);
            }
            // 더 작거나 같으면 카운팅만
            else{
                cnt += 1;
            }
        }
        // 마지막 카운팅 결과 저장
        result.add(cnt);
        return result.stream()
            .mapToInt(x->x)
            .toArray();
    }
}