import java.util.*;
class Task implements Comparable<Task>{
    int length;
    int time;
    int id;
    public Task(int length, int time, int id){
        this.length = length;
        this.time = time;
        this.id = id;
    }
    
    @Override
    public int compareTo(Task task){
        if(this.length != task.length){ 
            // 소요시간 비교
            return this.length - task.length;    
        }
        else{
            if(this.time != task.time){
                // 요청 시각 비교
                return this.time - task.time;
            }
            else{
                return this.id - task.id;
            }
        }
    }
    @Override
    public String toString(){
        return "id:" + this.id + " 소요시간:" + this.length + " 요청시간:" + this.time;
    }
    
}
class Solution {
    public int solution(int[][] jobs) {
        /*
        job에 id를 붙여서 Tasks로 저장
        Task를 먼저 요청 시점기준으로 오름차순 정렬
        그다음 매 1초마다 요청시점의 작업 Heap에 넣기
        
        아 근데 요청 시점이 이르면 애초에 먼저 실행되니까 굳이 정렬기준에 넣을 필요도 없을 듯?
        아니지 작업 중일 때 대기큐로 들어갈 수 있으니 정렬 기준에 유지는 해야함
        
        그냥 1초씩 지나가면서 해도 될듯 1000초니까
        */
        int reqSum = 0;
        List<Task> tasks = new ArrayList<>();  
        for(int i=0; i<jobs.length; i++){
            tasks.add(new Task(jobs[i][1], jobs[i][0], i));
            reqSum += jobs[i][0];
        }
        Collections.sort(tasks, Comparator.comparing(x -> x.time));
        // for(int i=0; i<tasks.size(); i++){
        //     System.out.println(tasks.get(i));    
        // }
        PriorityQueue<Task> heap = new PriorityQueue<>();
        // job을 넣고 job이 끝나는 시점 >= tasks의 time일 때 까지 tasks에서 poll해서 넣기
        int j=0;
        int cur = tasks.get(j).time;
        while(j < tasks.size() && tasks.get(j).time <= cur){
            heap.offer(tasks.get(j++));
        }
        int result = 0;
        Task curTask;
        while(!heap.isEmpty()){
            // 우선순위큐에서 작업 하나 꺼내서 진행하기
            curTask = heap.poll();
            //System.out.println(curTask);
            cur += curTask.length;
            result += cur;
            // 현재 시점까지 요청한 작업 우선순위 큐에 채우기
            while(j < tasks.size() && tasks.get(j).time <= cur){
                heap.offer(tasks.get(j++));
            }
            // 작업이 끝났는데 큐에 작업이 없으면 다음 작업 가져오기
            if(heap.isEmpty() && j < tasks.size()){
                Task next = tasks.get(j++);
                cur = next.time;
                heap.offer(next);
            }
        }
        //System.out.println((result - reqSum)/tasks.size());
      
        return (int)((result - reqSum)/tasks.size());
    }
}