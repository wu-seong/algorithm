import java.util.*;
class Solution {
    public int[] solution(int k, int[] score) {
        /*
        자기보다 더 큰 수가 있는 인덱스를 찾기 
        찾으면 해당 인덱스 + 1에 삽입
        0까지 못찾으면 0에 삽입
        
        크기가 k보다 크면 마지막 수 remove
        */
        List<Integer> result = new ArrayList<>();
        List<Integer> scores = new ArrayList<>();
        for(int s: score){
            boolean isMax = true;
            for(int j=scores.size()-1; j >=0; j--){
                // 발표점수보다 더 크면
                if(scores.get(j) > s){
                    scores.add(j+1, s);
                    isMax = false;
                    break;
                }
            }
            if(isMax){
                scores.add(0,s);
            }
            
            if(scores.size() > k){
                scores.remove(k);
            }
            result.add(scores.get(scores.size() - 1));
        }
        
        return result.stream()
            .mapToInt(i->i).toArray();
    }
}