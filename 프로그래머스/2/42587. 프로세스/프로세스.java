import java.util.*;
import java.util.stream.*;

class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public int solution(int[] priorities, int location) {
        int n = priorities.length;
        int[][] indexPriorities = new int[n][2]; //[0]: index, [1]: 우선순위
        for(int i=0; i<n; i++){
            indexPriorities[i][0] = i;
            indexPriorities[i][1] = priorities[i];
        }
        
        Queue<int[]> queue = new LinkedList<>();
        for(int i=0; i<n; i++){
            queue.offer(indexPriorities[i]);
        }
        // for(int[] process: queue){
        //     log(process[0]);
        //     log(process[1]);
        // }
        List<Integer> result = new ArrayList<>(); 
        // queue에서 꺼내기
        while(!queue.isEmpty()){
            for(int[] process: queue){
                log(process[0] + ": " + process[1]);
            }
            int[] process = queue.poll();
            int p = process[1];
            int l = process[0];
            // 마지막 작업일 때
            if(queue.isEmpty()){
                result.add(l);
                break;
            }
            int max = queue.stream()
                .mapToInt(x -> x[1])
                .max()
                .getAsInt();
            if(max > p){
                queue.offer(process);
            }
            else{
                result.add(l);
            }
        }
        for(int l: result){
            log(l);
        }
        // 더 높은 것 있는지 판단해서 있으면 다시 넣기, 없으면 결과 배열에 index 넣기
        // 결과 배열에서 location 순서 찾기
        for(int i=0; i<n; i++){
            if(result.get(i) == location){
                return i+1;
            }
        }
        return 0;
    }
}