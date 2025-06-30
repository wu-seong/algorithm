import java.util.*;

class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        /*
        각 사람의 점수를 map에 담기
        점수가 없는 경우에는 0
        */
        Map<String, Integer> score = new HashMap<>();
        int n = name.length;
        for(int i=0; i<n; i++){
            score.put(name[i], yearning[i]);
        }
        // for(String key: score.keySet()){
        //     log(key + " " + score.get(key));
        // }
        int[] result = new int[photo.length];
        for(int i=0; i<photo.length; i++){
            String[] people = photo[i];
            int sum = 0;
            for(String p: people){
                sum += score.getOrDefault(p, 0);
            }
            result[i] = sum;
        }
        return result;
    }
}