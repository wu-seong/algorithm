import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        /*
        오름차순 정렬 후
        
        각 번호를 
        시작점은 고정하고 길이별로 나눈 것을 set에 비교하기 
        있으면 바로 false임
        
        마지막에 모두 없으면 본인도 다시 넣기
        */
        Arrays.sort(phone_book, Comparator.comparingInt(String::length));
        Set<String> pre = new HashSet();
        for(String phone_num: phone_book){
            //System.out.println(phone_num);
            for(int i=1; i<=phone_num.length(); i++){
                String sub = phone_num.substring(0,i);
                if(pre.contains(sub)){
                    return false;
                }
            }
            pre.add(phone_num);
            //System.out.println(pre);
        }
        return true;
    }
}