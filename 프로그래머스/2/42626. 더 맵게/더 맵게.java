import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        /*
        log2 1000000 = log 2 2**20 = 약 20
        heapify
        2000만
        +
        최초에 heappop하여 1개를 가져온다
        가장 맵지 않은 것이 K 이상이면 섞지 않아도 된다. ->
        가장 맵지 않은 것이 K 미만이면
        그다음 맵지 않은 것도 pop해서
        새로운 음식을 만들어 heappush한다.
        만약 heap이 하나 남았는데 해당 음식이 K 미만이라면 -1 리턴
        2000만
        */
        PriorityQueue<Integer> heap = new PriorityQueue();
        for(int s: scoville){
            heap.offer(s);
        }
        // System.out.println(heap);
        int result = 0;
        while(!heap.isEmpty()){
            // 하나 꺼내서 확인
            int last = heap.poll();
            //System.out.println(last);
            if(last >= K){
                return result;
            }
            // 하나 더 꺼내서 만들기, 못 꺼내면 -1
            if(heap.isEmpty()){
                return -1;
            }
            int last2 = heap.poll();
            result += 1;
            heap.offer(last + last2*2);
        }
        return result;
    }
}