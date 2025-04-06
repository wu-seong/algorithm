class Solution {
    public static int maxDepth;
    public static int target;
    public static int cnt;
    public static void log(Object o){
        System.out.println(o);
    }
    public void dfs(int[] numbers, int depth, int sum){
        if(depth == maxDepth){
            if(sum == target){
                cnt += 1;
            }
            return;
        }
        // 현재숫자를 다음 재귀에 반영
        dfs(numbers, depth+1, sum + numbers[depth]);
        dfs(numbers, depth+1, sum - numbers[depth]);
    }
    public int solution(int[] numbers, int target) {
        // 더하거나 빼거나 해서 마지막에 도달했을 때 합을 구해서 target과 비교
        maxDepth = numbers.length;
        int answer = 0;
        this.target = target;
        dfs(numbers, 0, 0);
        log(cnt);
        return cnt;
    }
}