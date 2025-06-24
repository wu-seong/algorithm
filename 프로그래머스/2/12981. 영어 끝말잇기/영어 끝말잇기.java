import java.util.*;
class Solution {
    public int[] solution(int n, String[] words) {
        /*
        끝말잇기 규칙
        탈락한 사람의 번호/회차
        
        1. 이전 단어의 마지막 단어와 일치여부 확인
        2. 중복 여부 확인
        
        words를 순회하면서 순서와 회차 카운팅
        
        끝까지 지켰으면 [0,0]
        */
        Set<String> used = new HashSet<>();
        
        int order = 0;
        int round = 0;
        char last = '\0';
        for(String word: words){
            order %= n;
            // 순서가 돌아옴
            if(order == 0){
                round += 1;
            }
            //System.out.println(order +" " + round);
            char first = word.charAt(0);
            // 규칙 위반
            if(!(last == '\0' || last == first) || used.contains(word)){
                return new int[]{order+1, round};
            }
            last = word.charAt(word.length()-1);
            order++;
            used.add(word);
        }
        return new int[]{0,0};
    }
}