import java.util.*;
class Solution {
    public int solution(int[] elements) {
        /*
        길이가 1 ~ n까지인 부분수열 순차적으로 구해서 저장
        n번째 길이면 n-1 번째 것 이전에 구한 합에 더하기
        */
        Set<Integer> score = new HashSet<>();
        int n = elements.length;
        int[] sum = new int[n];
        for(int i=0; i<n; i++){ // 더할 인덱스
            for(int j=0; j<n; j++){ // 시작 인덱스
                sum[j] += elements[(j+i)%n];
                if(!score.contains(sum[j])){
                    score.add(sum[j]);
                }
            }
        }
        return score.size();
    }
}