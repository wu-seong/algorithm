import java.util.*;

class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public String solution(String[] participant, String[] completion) {
        // participant 돌면서 Map에 카운팅
        HashMap<String, Integer> pCnt = new HashMap<>();
        for(String name: participant){
            if(pCnt.containsKey(name)){
                pCnt.put(name, pCnt.get(name) + 1);
            }
            else{
                pCnt.put(name, 1);    
            }
        }
        
        // completion 돌면서 역 카운팅
        for(String name: completion){
            pCnt.put(name, pCnt.get(name) - 1);
        }        
        
        // 0이 아닌 참가자 찾아서 리턴
        for(String name: pCnt.keySet()){
            if(pCnt.get(name) != 0){
                return name;   
            }
        }   
        return null;
    }
}