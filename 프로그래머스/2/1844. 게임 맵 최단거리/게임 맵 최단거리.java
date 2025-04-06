import java.util.*;

class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public int bfs(int[][] map, int startY, int startX, int endY, int endX){
        boolean[][] visited = new boolean[endY+1][endX+1];
        Queue<int[]> queue = new LinkedList<>();
        int[] start = {startY, startX, 0};
        queue.offer(start);
        visited[startY][startX] = true;
        
        
        while(!queue.isEmpty()){
            int[] cur = queue.poll();
            // log(cur.get(0) + " " +cur.get(1));
            if(cur[0] == endY && cur[1] == endX){
                return cur[2] + 1;
            }
            int[][] directions = {
                {1,0}, {0,1},{-1,0},{0,-1}
            };
            for(int[] d: directions){
                int dy = d[0], dx = d[1];
                int yy = cur[0] + dy, xx = cur[1] + dx;
                if( (0<= yy && yy <= endY) && (0<= xx && xx <= endX) && map[yy][xx] == 1){
                    if(!visited[yy][xx]){
                        queue.offer(new int[]{ yy, xx, cur[2]+1 });
                        visited[yy][xx] = true;
                    }
                    
                }
            }
        }
        return -1;
    }
    public int solution(int[][] maps) {
        //bfs
        int n = maps.length, m = maps[0].length;
        int result = bfs(maps, 0,0, n-1,m-1);
        log(result);
        return result;
    }
}