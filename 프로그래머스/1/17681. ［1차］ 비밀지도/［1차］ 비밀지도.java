import java.util.*;
import java.util.stream.*;
class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] result = new String[n];
        for(int i=0; i<n; i++){
            // 이진문자열 변환
            String temp = Integer.toBinaryString(arr1[i] | arr2[i]);
            
            // 치환
            temp = temp.replace("1","#").replace("0"," ");
            // 공백 채우기
            // for(int j=0; j<n-temp.length(); j++){
            //     temp = ' ' + temp;
            // }
            result[i] = String.format("%" + n + "s", temp);
            //System.out.println(temp[i]);
        }
        return result;
    }
}