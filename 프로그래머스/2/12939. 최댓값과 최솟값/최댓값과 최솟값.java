import java.util.*;
class Solution {
    public String solution(String s) {
        /*
        " "으로 스플릿해서 string 만든 뒤에 Integer.parseInt해서 정수배열로 바꾸기
        stream 이용해서 max, min 쓰기?
        */
        String[] sArray = s.split(" ");
        Integer[] intArray = new Integer[sArray.length];
        for(int i=0; i<sArray.length;i++){
            intArray[i] = Integer.parseInt(sArray[i]);
            System.out.println(intArray[i]);
        }
        int max = Arrays.stream(intArray).max(Integer::compare).get();
        int min = Arrays.stream(intArray).min(Integer::compare).get();
        
        
        return Integer.toString(min) + " " + Integer.toString(max);
    }
}