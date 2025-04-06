class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public int solution(int[][] sizes) {
        /*
        가장 큰 길이를 구하고
        가로 세로 중 큰 쪽을 그 길이로 커버 
        가로 세로 중 더 작은 것 중 가장 큰 것을 구하기
        */
        int n = sizes.length;
        int a,b;
        // 가장 큰 길이 구하기
        int most = 0;
        for(int i=0; i<n; i++){
            a = sizes[i][0];
            b = sizes[i][1];
            most = Math.max(most, a);
            most = Math.max(most, b);
        }
        // log(most);
        
        // 가로 세로 중 더 작은 것 중 가장 큰 것
        int max = 0;
        for(int i=0; i<n; i++){
            a = sizes[i][0];
            b = sizes[i][1];
            int lower = Math.min(a, b);
            max = Math.max(max, lower);
        }
        log(max + " " + most);
        return max*most;
    }
}