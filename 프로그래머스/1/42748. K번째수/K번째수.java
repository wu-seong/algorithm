import java.util.*;

class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public int[] solution(int[] array, int[][] commands) {
        /*
        1. commands에서 받은 범위로 원본 문자열을 자르고 정렬 하기
        2. k-1 번째 인덱스 수 구해서 result에 넣기
        */
        int n = commands.length;
        int[] result = new int[n];
        for(int i=0; i< n; i++){
            int start = commands[i][0];
            int end = commands[i][1];
            int target = commands[i][2];
            int[] sub = Arrays.copyOfRange(array, start-1, end);
            Arrays.sort(sub);
            result[i] = sub[target-1];
        }
        return result;
    }
}