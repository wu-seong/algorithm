import java.util.*;
class Solution {
    /*
    공백 기준 앞이 D인지 아닌지
    */
    
    public static void interPrinter(String command, PriorityQueue<Integer> maxHeap, PriorityQueue<Integer> minHeap, Map<Integer,Integer> counter){
        String[] str = command.split(" ");
        if(str[0].equals("D")){
            if(str[1].equals("1")){
                while(!maxHeap.isEmpty()){
                    int value = maxHeap.poll();
                    int cnt = counter.get(value);
                    if(cnt > 0){
                        //System.out.println("최댓값 추출" + value + " -> " + (cnt-1));
                        counter.put(value, cnt - 1);
                        break;
                    }
                }
            }
            else{
                while(!minHeap.isEmpty()){
                    int value = minHeap.poll();
                    int cnt = counter.get(value);
                    if(cnt > 0){
                        //System.out.println("최솟값 추출" + value + " -> " + (cnt-1));
                        counter.put(value, cnt - 1);
                        break;
                    }
                }
            }
        }
        else{
            // push 하는 경우
            int num = Integer.parseInt(str[1]);
            maxHeap.offer(num);
            minHeap.offer(num);
            if(counter.containsKey(num)){
                counter.put(num, counter.get(num) + 1);
            }
            else{
                counter.put(num, 1);
            }
        }
    }
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> minHeap = new PriorityQueue();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a,b) -> b-a);
        Map<Integer, Integer> counter = new HashMap<>();
        
        
        for(String s: operations){
            interPrinter(s, maxHeap, minHeap, counter);
        }
        //counter.forEach((k,v) -> System.out.println(k + " = " + v));
        int max = 0;
        int min = 0;

        // max 값 꺼내기
        while (!maxHeap.isEmpty()) {
            int value = maxHeap.peek();
            if (counter.getOrDefault(value, 0) > 0) {
                max = value;
                break;
            } else {
                maxHeap.poll(); // 쓰레기값 버리기
            }
        }

        // min 값 꺼내기
        while (!minHeap.isEmpty()) {
            int value = minHeap.peek();
            if (counter.getOrDefault(value, 0) > 0) {
                min = value;
                break;
            } else {
                minHeap.poll(); // 쓰레기값 버리기
            }
        }

        
        return new int[]{max, min};
    }
}