import java.util.*;
class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public int[] solution(String s) {
        /*
        순회하면서 Map에 각 문자별 위치를 저장하고 없으면 0 저장 있으면 현재 인덱스 계산하고 갱신
        */
        Map<Character, Integer> location = new HashMap();
        int[] result = new int[s.length()];
        int i=0;
        for(char c: s.toCharArray()){
            if(!location.containsKey(c)){
                result[i++] = -1;   
            }
            else{
                int last = location.get(c);
                result[i++] = i - last;
            }
            location.put(c, i);
        }
        // for(int n: result){
        //     log(n);
        // }
        return result;
    }
}