import java.util.*;

class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public static String intToBinary(int num){
        // 2 mod 연산 값 구하기
        // 2 나누기
        // 몫이 2보다 작으면 끝 
        
        StringBuilder b = new StringBuilder();
        while(num >= 2){
            int remain = num % 2;
            b.append(remain);
            num = num / 2;
        }
        b.append(num);
        b.reverse();
        return b.toString();
    }
    public int[] solution(String s) {
        /*
        한사이클 마다 
        1. 0 개수 구하기, result에 저장
        2. 전체 길이에서 0 개수 빼기
        3. 구한 값 이진수 변환하기
        
        --> 전체 길이가 1이 될 때 까지 반복
        */
        int cnt = 0;
        int total = 0;
        while(s.length() >= 2){
            cnt++;
            int zero = 0;
            for(int i=0; i<s.length(); i++){
                if(s.charAt(i) == '0'){
                    zero++;
                }
            }
            //log(zero);
            int temp = s.length() - zero;
            total += zero; 
            s = intToBinary(temp);
        }
        return new int[]{cnt, total};
    }
}